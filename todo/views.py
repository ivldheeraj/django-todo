from django.shortcuts import render,redirect
from django.http import HttpResponse
from .form import TodoForm
from .models import Todo 

def todo_list(request):
    #return HttpResponse("HelloWorld")
    todos = Todo.objects.all()
    #print(todos)
    context = {
        "todo_list" : todos
    }
    return render(request,"todo.html",context)


def todo_detail(request, id):
    todo =Todo.objects.get(id=id)
    context = {
         "todo" : todo
    }
    return render(request,"todo_detail.html",context)


def todo_create(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        #create todo obj
       form.save()
       return redirect('/')
    context = {"form": form}
    return render(request,'todo_create.html',context)


def todo_update(request,id):
    todo =Todo.objects.get(id=id)
    form = TodoForm(request.POST or None,instance=todo)
    if form.is_valid():
        #create todo obj
       form.save()
       return redirect('/')
    context = {"form": form}
    return render(request,'todo_update.html',context)

def todo_delete(request,id):
    todo =Todo.objects.get(id=id)
    todo.delete()
    return redirect("/")

