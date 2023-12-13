from django.shortcuts import render,redirect
from .models import Todo
from django.http import HttpResponse
# Create your views here.

def home(request):
    
    if request.method=='POST':
        Todo.objects.create(
            todo=request.POST.get('todo')
        )
    data=Todo.objects.all()
    return render(request,'todoapp/home.html',{'data':data})

def deletetodo(request,pk):
    deltodo=Todo.objects.get(id=pk)
    deltodo.delete()
    return redirect('home')

# def updatepage(request,pk):
#     updatetodo=Todo.objects.get(id=pk)
#     return render(request,'todoapp/update.html',{'updatetodo':updatetodo})



def updatetodo(request,pk):
    updatetodo=Todo.objects.get(id=pk)
    if request.method=='POST':
        updatetodo.todo=request.POST.get('todo')
        updatetodo.save()
    return redirect('home')
    
   
    