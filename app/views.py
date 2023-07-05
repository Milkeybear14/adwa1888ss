from django.shortcuts import render
from .models import what_we_do,why_choose_us,clients_response,year
from about.models import about_company,contact
from portfolio.models import portfolios
# Create your views here.
def index(request):
    works = what_we_do.objects.all()
    abouts = about_company.objects.all()
    contacts = contact.objects.all()
    portfolio = portfolios.objects.all()
    choice = why_choose_us.objects.all()
    responses = clients_response.objects.all()
    years = year.objects.all()
    return render(request,"index.html", {
    'welcome_message':"Hello Adwayans",
    'works':works,
    'about':abouts,
    'contacts':contacts,
    'portfolios':portfolio,
    'choices':choice,
    'responses':responses,
    'years':years})
