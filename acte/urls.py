from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from acte.models import Document, Institution
from . import views

urlpatterns = [
   url(r'^$' , views.index , name ='index'),
   url(r'^categorii$', views.categorii, name = 'categorii'),
   url(r'^acte$', ListView.as_view(queryset=Document.objects.all().order_by("id"),template_name="acte/home.html")),
   url(r'^institutii$', ListView.as_view(queryset=Institution.objects.all().order_by("id"),template_name="acte/home.html")),


# Add the rest of the URLs
   ]
