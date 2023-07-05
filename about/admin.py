from django.contrib import admin
from .models import about_company
from .models import contact

# Register your models here.
admin.site.register(about_company)
admin.site.register(contact)