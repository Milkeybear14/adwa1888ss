from django.shortcuts import render
from app.models import what_we_do
from about.models import about_company
from about.models import contact
# Create your views here.
def we_do(request):
    works = what_we_do.objects.all()
    about = about_company.objects.all()
    contacts = contact.objects.all()
    return render(request,"we_do.html",{'works':works,'about':about,'contacts':contacts})