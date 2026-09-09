from django.shortcuts import render

# Create your views here.
from .models import Task

def task_list(request):
    tasks = Task.objects.all().order_by('due_date')

    context = {'tasks' : tasks}
    return render(request, 'task_list.html', context)