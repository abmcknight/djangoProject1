from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import Todo
# Create your views here.


def index(request):
    form = TodoForm
    todo = Todo.objects.all()
    context = {'form': form, 'todo': todo}
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        return render(request, 'todo/index.html', context)


def update(request, id):
    todo = Todo.objects.get(id=id)
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect('index')

    context = {'form': form}
    return render(request, 'todo/update.html', context)


def delete(request, id):
    todo = Todo.objects.get(id=id)
    if request.method == 'POST':
        todo.delete()
        return redirect('index')
    context = {'todo': todo}
    return render(request, 'todo/delete.html', context)


def complete_task(request, id):
    task = Todo.objects.get(id=id)
    task.completed = True
    task.save()
    return redirect('index')
