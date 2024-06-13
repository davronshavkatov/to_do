
from django.shortcuts import render
from task.models import Task

def home (request):
    tasks = Task.objects.filter(is_complected=False)
    completed_tasks = Task.objects.filter(is_complected=True)
    context = {
        'tasks':tasks,
        'completed_tasks':completed_tasks
    }
    return render(request, 'home.html', context)