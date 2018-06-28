from django.shortcuts import render, redirect

def home(request):
    return redirect('index/')

def index(request):
    return render(request, 'index.html', {})
