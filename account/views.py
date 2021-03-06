# -*- coding: utf-8 -*-
from __future__ import unicode_literals

##Import Django library
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views import generic

def home(request):
    ''' home : home page view
            Templates: home.html
            Request_path: '/'
            Context: N/A
    '''
    return render(request, 'home.html')

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'