# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from app1.models import AccessRecord, Topic, Webpage, User
from . import forms

# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    website_Urls = Webpage.objects.all()
    top = Topic.objects.all()

    date_dict = {'access_records': webpages_list, 'top': top, 'web': website_Urls}
    
    return render(request, 'app1/index.html', context=date_dict)

def help(request):
    help_dict = {
        'help_var': 'This help text is from Django !!',
        'help_var2': 'Second veriable from Django',    
    }
    return render(request,'app1/help.html',context=help_dict)

def users(request):
    users = User.objects.all()
    form = forms.UserForm()

    if request.method == "POST":
        form = forms.UserForm(request.POST)
        
        if form.is_valid:   
            form.save()
            return index(request)
        
        else:
            print("Error occured while saving form")

    u_dict = {"users": users, "user_Form": form}

    return render(request,"app1/users.html",u_dict)
