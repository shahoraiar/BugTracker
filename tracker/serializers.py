
from rest_framework import serializers
from .models import Project, Bug

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"
        read_only_fields = ["owner", "created_at", "updated_at"]  

class BugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bug
        fields = "__all__"
        read_only_fields = ["created_by", "created_at", "updated_at"]  