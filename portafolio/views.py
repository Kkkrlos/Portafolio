from django.shortcuts import render, redirect
from .models import Project

def index(request):
    projects = Project.objects.all()

    return render(request, 'index.html', {'projects': projects})

def Linkedin(request):
    return redirect('https://www.linkedin.com/in/carlosrodriguez1205/')

def Github(request):
    return redirect('https://github.com/Kkkrlos')