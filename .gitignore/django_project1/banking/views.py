# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import UserLogin,UserLogout,Authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from .forms import UserRegisterForm,UserUpdateForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated!'.format())
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form,
    }

    return render(request, 'users/profile.html', context)

def login(request):
	username_temp = request.POST.get('username', '')
	password_temp = request.POST.get('password', '')
	user = Authenticate(request, username = username_temp, password = password_temp)
	if user is not None:
		UserLogin(request, user)
		return JsonResponse( {'message': 'Successful login!', 'balance': user.profile.balance}, status = 200 )
	else:
		return JsonResponse( {'error': 'Invalid details!'}, status = 401 )
 def logout(request):
	UserLogout(request)
	return JsonResponse({})


def check_session(request):
	return JsonResponse( {'username': request.user.username, 
		'first_name': request.user.profile.first_name,
		}, )


def get_balance(request):
	if not request.user.is_authenticated:
		return JsonResponse({
			'error': 'Get Lost'
		})
	return JsonResponse({
		'balance': request.user.profile.balance,
		})


def withdraw(request):
	user = request.user
	print(user.is_authenticated)
	if not request.user.is_authenticated:
		return JsonResponse({
			'error': 'Get Lost'
			})
	withdraw_amount = int(request.POST.get('amount', ''))
	#print(request.POST)
	cur_balance = user.profile.balance
	if withdraw_amount > cur_balance:
		return JsonResponse({
			'error': 'Insufficient Funds!'
			})
	else:
		user.profile.balance = user.profile.balance - withdraw_amount
		user.save()
		return JsonResponse({
			'message': 'Withdrawing is Successful',
			'new_balance': user.profile.balance,
			})

def deposit(request):
	if not request.user.is_authenticated:
		return JsonResponse({
			'error': 'Get Lost'
		})
	user = request.user
	deposit_amount = int(request.POST.get('amount', ''))
	user.profile.balance = user.profile.balance + deposit_amount
	user.save()
	return JsonResponse({
		'message': 'Deposit is Successful',
		'new_balance': user.profile.balance,
		})
# Create your views here.
