from django.contrib import admin
from .models import Project, Tag, Task, RecurringTask, Notification

admin.site.register(Project)
admin.site.register(Tag)
admin.site.register(Task)
admin.site.register(RecurringTask)
admin.site.register(Notification)