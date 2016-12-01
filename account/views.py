#coding:utf-8
from __future__ import unicode_literals
from django.conf import settings
from django.http import HttpResponseRedirect, QueryDict
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import resolve_url

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(resolve_url(settings.LOGIN_REDIRECT_URL))
                    #return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return render(request, 'account/login.html',{'msg':'用户名密码错误'})

    else:
        return render(request, 'account/login.html')


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # Create the user profile
            profile = Profile.objects.create(user=new_user)
            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    #return render(request, 'account/register.html', {'user_form': user_form})
    return render(request, 'account/register.html')

def forgetpass(request):
    return HttpResponse('该功能还未实现！')

@login_required
def dashboard(request):
    return render(request, 'base2.html', {'section': 'dashboard'})