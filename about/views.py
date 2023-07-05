from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import about_company
from .models import contact
# Create your views here.
def about(request):
    about = about_company.objects.all()
    contacts = contact.objects.all()
    return render(request,"about.html",{'about':about,'contacts':contacts})
    