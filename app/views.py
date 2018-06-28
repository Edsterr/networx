from django.shortcuts import render, redirect

def home(request):
    return redirect('index/')

def index(request):
    return render(request, 'index.html', {})

def search(request):
	return render(request, 'search.html')

def profile(request):
	return render(request, 'profile.html')

def register(request):
	return render(request, 'register.html')