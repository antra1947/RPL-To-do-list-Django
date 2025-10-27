from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.utils import timezone


def task_list(request):
    tasks = Task.objects.all().order_by('due_date')
    return render(request, 'myapp/task_list.html', {'tasks': tasks})


def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST.get('description', '')
        status = request.POST.get('status', 'Pending')
        due_date = request.POST.get('due_date', timezone.now().date())
        is_completed = True if request.POST.get('is_completed') == 'on' else False
        Task.objects.create(
            title=title,
            description=description,
            status=status,
            due_date=due_date,
            is_completed=is_completed
        )
        return redirect('task_list')
    return render(request, 'myapp/task_form.html')


def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST.get('description', '')
        task.status = request.POST.get('status', 'Pending')
        task.due_date = request.POST.get('due_date', timezone.now().date())
        task.is_completed = True if request.POST.get('is_completed') == 'on' else False
        task.save()
        return redirect('task_list')
    return render(request, 'myapp/task_form.html', {'task': task})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')

def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'myapp/task_detail.html', {'task': task})
