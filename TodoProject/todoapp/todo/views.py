from django.shortcuts import render,redirect
from django.http import  HttpResponseRedirect
from .forms import FormTodo
from .models import  Todo
# Create your views here.

def delete(request,id):
    print(id)
    Todo.objects.get(id=id).delete()
    return HttpResponseRedirect("/")

def index(request):
    data=Todo.objects.order_by('-id')
    form=FormTodo()
    if request.method == 'POST':
        form=FormTodo(request.POST)
        if form.is_valid():
            form.save(commit=True)
    return render(request,'index.html',{'form':form,'data':data})
