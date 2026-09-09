from django.shortcuts import render
from flask import request

# Create your views here.
from .models import Task

def task_list(request):
    tasks = Task.objects.all().order_by('due_date')

    task_table = {'tasks' : tasks}
    return render(request, 'task_list.html', task_table)