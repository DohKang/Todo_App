from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin): #overwriting
    list_display = ('task', 'is_completed', 'modified_at')
    search_fields = ('task',)
admin.site.register(Task, TaskAdmin)