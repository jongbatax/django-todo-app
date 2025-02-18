from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import TodoForm
from .models import Todo


def todo_home(request):
    form = TodoForm()
    todos = Todo.objects.all()

    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("todo_home")

    context = {
        "todos": todos,
        "form": form,
    }

    return render(request, "todo_app/index.html", context)


def update_status(request):
    if request.method == "POST":
        todo_id = request.POST["todo_id"]
        todo = get_object_or_404(Todo, pk=todo_id)

        todo.status = not todo.status
        todo.save()
        return redirect("todo_home")
    else:
        return redirect("todo_home")


def delete_todo(request):
    if request.method == "POST":
        todo_id = request.POST["delete_id"]
        todo = get_object_or_404(Todo, pk=todo_id)

        todo.delete()
        return redirect("todo_home")
    else:
        return redirect("todo_home")


def edit_todo(request, id):
    todo = get_object_or_404(Todo, pk=id)
    form = TodoForm(instance=todo)
    context = {"todo": todo, "form": form}
    return render(request, "todo_app/update.html", context)


def update_todo(request):
    todo = get_object_or_404(Todo, pk=request.POST["todo_id"])

    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)

        if form.is_valid():
            form.save()
        return redirect("todo_home")
