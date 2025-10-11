from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, TagViewSet, TaskViewSet
router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'tag', TagViewSet)
router.register(r'task', TaskViewSet)
urlpatterns = [
    path('', include(router.urls))
]