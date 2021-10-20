from django.shortcuts import render

# Create your views here.
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from .forms import UserForm
from django.contrib.auth.decorators import login_required
from .models import User


def Base(request):
    return render(request, "base.html")


'''
def Add(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            form = UserForm()
        else:
            form = UserForm()
        da = User.objects.all()
        return render(request, 'show.html', {"form": form, "da": da})

    form = UserForm(request.POST or None)
'''


def Add(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = UserForm()
    da = User.objects.all()
    return render(request, 'show.html', {"form": form, "da": da})


def Delete(request, pk):
    if request.method == "POST":
        pi = User.objects.get(pk=pk)
        pi.delete()
    return HttpResponseRedirect("/crud/add/")

def Edit(request, pk):
    if request.method == "POST":
        pi = User.objects.get(pk=pk)
        fm = UserForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
     pi = User.objects.get(pk=pk)
     fm = UserForm(instance=pi)
    return render(request, 'edit.html', {"form": fm})




