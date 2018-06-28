from django.shortcuts import render, redirect
from app.models import User, Skills
from django.contrib.auth.decorators import login_required
from app.forms import ModelForm

def home(request):
    return redirect('index/')

def index(request):
    return render(request, 'index.html', {})

def search(request):
	return render(request, 'search.html')

def profile_id_func(request, profile_id):
	profile_details = User.objects.filter(sid=profile_id)
	print(profile_details)

	contextDict = {'profile_details': []}
	contextDict['profile_details'] = {'sid': profile_details.sid, 'name': profile_details.name, 'location': profile_details.location, 'floor': profile_details.floor, 'skills': profile_details.skills}

	return render(request, 'profile.html', context=contextDict)

def register(request):
	form = ModelForm(request.POST)

	if form.is_valid():
		form.save()
		return redirect('/search')

	return render(request, 'register.html', {'form': form})