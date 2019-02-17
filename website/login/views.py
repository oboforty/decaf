from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.models import User
from .models import DoctorUser

@login_required(login_url='/user/login')
def home(request):
	return render(request, 'home.html',{'username': request.user.username})

def mylogin(request):
	if request.method == 'GET':
		return render(request, 'login.html')

	elif request.method == 'POST':
		username = request.POST.get('username','')
		password = request.POST.get('password','')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			# the url name 'home' under 'login' app
			return redirect(reverse('login:home'))
		else:
			return render(request, 'login.html', {'username': username, 'password': password,})

def register(request):
	if request.method == 'GET':
		return render(request, 'register.html')
	username = request.POST.get('username','')
	password = request.POST.get('password','')
	user = DoctorUser.objects.create_user(username, '', password)
	user.save()
	return redirect(reverse('login:login'))

@login_required(login_url='/user/login')
def change_password(request):
	if request.method == 'GET':
		return render(request, 'change_password.html',{'username': request.user.username})
	username = request.user.username
	password = request.POST.get('password','')
	user = DoctorUser.objects.get(username=username)
	user.set_password(password)
	user.save()
	logout(request)
	return redirect(reverse('login:login'))

def mylogout(request):
	logout(request)
	return redirect(reverse('login:login'))

