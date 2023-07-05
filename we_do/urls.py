from django.urls import path,include

from . import views

urlpatterns = [
    path("we_do",views.we_do,name="we_do"),
]