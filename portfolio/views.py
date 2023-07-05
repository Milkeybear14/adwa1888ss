from django.shortcuts import render
from .models import portfolios
from about.models import about_company,contact

# Create your views here.
def portfolio(request):
    portfolio = portfolios.objects.all()
    abouts = about_company.objects.all()
    contacts = contact.objects.all()
    return render(request,"portfolio.html",{'portfolios':portfolio,'about':abouts,'contacts':contacts})