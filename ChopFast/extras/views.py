from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Tasks
from .forms import TaskUpdateForm, AddTask


@login_required(login_url="/login/")
def updateTask(request, id):
    task = Tasks.objects.get(id=id)
    if request.method == "POST":
        form = TaskUpdateForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
    else:
        form = TaskUpdateForm()
    return render(request, 'taskUpdate.html', {'form': form})


@login_required(login_url="/login/")
def addTask(request):
    if request.method == "POST":
        form = AddTask(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AddTask()
    return render(request, 'addtask.html', {'form': form})
# Create your views here.
