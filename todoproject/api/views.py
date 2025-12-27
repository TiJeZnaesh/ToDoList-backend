from rest_framework import viewsets
from .models import Project, Tag, Task, RecurringTask, Notification
from .serializers import ProjectSerializer, TagSerializer, TaskSerializer, TaskCreateSerializer, RecurringTaskSerializer, NotificationSerializer
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

class RecurringTaskViewSet(viewsets.ModelViewSet):
    queryset = RecurringTask.objects.all()
    serializer_class = RecurringTaskSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


