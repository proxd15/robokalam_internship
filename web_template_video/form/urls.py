from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path("formdb",views.forms,name="form"),
]