from django.contrib import admin

# Register your models here.
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_completed', 'due_date')
    list_filter = ('is_completed', 'category')
    search_fields = ('title', 'due_date',)