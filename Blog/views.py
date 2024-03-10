from Blog.forms import TodoForms, TodoUpdateForm
from Blog.models import Todo
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect, render

# Create your views here.


def hello_world(request):
    todo = Todo.objects.all()
    return render(request, "index.html", context={"todo1": todo})


def profile(request):
    return render(request, "profile.html", {"name": "sam"})


def detail(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    return render(request, "detail.html", {"todo": todo})


def delete(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    messages.success(request, "Todo is deleted successfully")
    return redirect("home")


def forms(request):
    if request.method == "POST":
        form = TodoForms(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Todo.objects.create(title=cd["title"], body=cd["body"], create=cd["create"])
            messages.success(request, "successfully added")
            return redirect("home")

    else:
        form = TodoForms()

        return render(request, "forms.html", {"form": form})


def update(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == "POST":
        form = TodoUpdateForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, "Your todo updated edit successfully")
            return redirect("details", todo_id)
    else:
        form = TodoUpdateForm(instance=todo)
        return render(request, "update.html", {"form": form})
