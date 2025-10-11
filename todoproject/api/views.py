from rest_framework import viewsets
from .models import Project, Tag, Task
from .serializers import ProjectSerializer, TagSerializer, TaskSerializer, TaskCreateSerializer
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return TaskCreateSerializer
        return TaskSerializer