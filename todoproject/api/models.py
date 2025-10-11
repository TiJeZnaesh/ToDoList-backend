from django.db import models
class Project(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название проекта")
    description = models.TextField(blank=True, verbose_name="Описание проекта")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    def __str__(self):
        return self.name
class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название тега")
    color = models.CharField(blank=True, max_length=20, verbose_name="Цвет тега")
    def __str__(self):
        return self.name
class Task(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название задачи")
    description = models.TextField(blank=True, verbose_name="Описание задачи")
    due_date = models.DateTimeField(verbose_name="Дата выполнения")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name="Проект")
    tags = models.ManyToManyField(Tag, blank=True, verbose_name="Теги")
    is_completed = models.BooleanField(default=False, verbose_name="Выполнена")
    def __str__(self):
        return self.title
