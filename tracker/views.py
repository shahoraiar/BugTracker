from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Project, Bug
from .serializers import ProjectSerializer, BugSerializer
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class BugViewSet(viewsets.ModelViewSet):
    queryset = Bug.objects.all()
    serializer_class = BugSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        bug = serializer.save(created_by=self.request.user)
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f"project_{bug.project.id}",
            {
                "type": "new_bug",
                "data": {
                    "title": bug.title,
                    "description": bug.description,
                    "status": bug.status,
                    "priority": bug.priority
                }
            }
        )


def bug_list_view(request, project_id):
    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        return HttpResponse("Project id not valid", status=404)

    bugs = project.bugs.order_by("-created_at").all()

    previous_bugs = [
        {
            "title": b.title,
            "status": b.status,
            "priority": b.priority,
            "description": b.description,
            "created_at": b.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        }
        for b in bugs
    ]

    return render(request, "bug_list.html", {
        "project_id": project.id,
        "project_name": project.name,
        "previous_bugs": previous_bugs,
    })
