from rest_framework import serializers
from .models import Project, Tag, Task
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name", "color"]
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["id", "name", "description", "created_at"]
class TaskSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    project = ProjectSerializer(read_only=True)
    class Meta:
        model = Task
        fields = ["id", "title", "description", "due_date", "tags", "created_at", "project", "is_completed"]
class TaskCreateSerializer(serializers.ModelSerializer):
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())
    class Meta:
        model = Task
        fields = ["id", "title", "description", "due_date", "tags", "created_at", "project", "is_completed"]