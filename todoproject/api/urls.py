from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, TagViewSet, TaskViewSet, RecurringTaskViewSet, NotificationViewSet
router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'tags', TagViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'recurring-tasks', RecurringTaskViewSet)
router.register(r'notifications', NotificationViewSet)
urlpatterns = [
    path('', include(router.urls))
]