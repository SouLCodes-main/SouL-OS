from django.shortcuts import render
from flask import request

# Create your views here.
from .models import Task

def task_list(request):
    tasks = Task.objects.all().order_by('due_date')

    context = {'tasks' : tasks}
    return render(request, 'todos/task_list.html', context)