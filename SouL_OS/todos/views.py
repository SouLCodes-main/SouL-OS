from django.shortcuts import redirect, render, get_object_or_404
from .models import Task
from .forms import TaskForm

def task_list(request):
    # form submission
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list') # Refresh the page to show the new task
    
    # Get request
    else:
        form = TaskForm()
    tasks = Task.objects.all().order_by('due_date')

    context = {'tasks' : tasks, 'form': form}
    return render(request, 'task_list.html', context)

def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.is_completed = not task.is_completed 
    task.save()
    return redirect('task_list')

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')

