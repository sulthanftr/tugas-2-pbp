import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect, response
from django.urls import reverse

from todolist.forms import TaskForm
from .models import Task

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')

    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_todolist"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('todolist:login')

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    try: 
        user = request.user
        data = Task.objects.filter(user=user)
        context = {
            'todolist': data,
            'nama': user.username,
            'last_login': request.COOKIES['last_login'],
        }
        return render(request, "todolist.html", context)
    except KeyError:
        return redirect('todolist:login')

@login_required(login_url='/todolist/login/')
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        form.instance.user = request.user
        form.instance.date = datetime.datetime.now()

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("todolist:show_todolist"))

    else:
        form = TaskForm()

        return render(request, 'create-task.html', {'form':form})

@login_required(login_url='/todolist/login/')
def task_selesai(request, pk):
    task = Task.objects.filter(id=pk).first()
    task.is_finished = True
    task.save()
    return HttpResponseRedirect(reverse("todolist:show_todolist"))

@login_required(login_url='/todolist/login/')
def undo_task(request, pk):
    task = Task.objects.filter(id=pk).first()
    task.is_finished = False
    task.save()
    return HttpResponseRedirect(reverse("todolist:show_todolist"))

@login_required(login_url='/todolist/login/')
def hapus_task(request, pk):
    Task.objects.filter(id=pk).first().delete()
    return HttpResponseRedirect(reverse("todolist:show_todolist"))