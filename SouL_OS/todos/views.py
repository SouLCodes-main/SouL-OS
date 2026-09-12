from django.shortcuts import redirect, render

# Create your views here.
from .models import Task
from .forms import TaskForm

def task_list(request):
    # Handle the form submission
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list') # Refresh the page to show the new task
    
    # If it's a GET request, just show the empty form
    else:
        form = TaskForm()
    tasks = Task.objects.all().order_by('due_date')

    context = {'tasks' : tasks, 'form': form}
    return render(request, 'task_list.html', context)

