from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from acte.models import Document, Institution
from . import views

urlpatterns = [
   url(r'^$' , views.index , name ='index'),
   url(r'^documente$', ListView.as_view(queryset=Document.objects.all().order_by("id"),template_name="acte/lista_acte.html")),
   url(r'^documente/(?P<slug>\d+)$', DetailView.as_view(model = Document, template_name="acte/act.html")),
   url(r'^institutii$', ListView.as_view(queryset=Institution.objects.all().order_by("id"),template_name="acte/lista_institutii.html")),
   url(r'^institutii/(?P<slug>[\w\-]+)/$', DetailView.as_view(model = Institution, template_name="acte/institutie.html")),
   url(r'^categorie/auto$', ListView.as_view(queryset=Document.objects.all().order_by("id"),template_name="acte/categorie.html")),
   url(r'^categorie/educational$', ListView.as_view(queryset=Document.objects.all().order_by("id"),template_name="acte/categorie.html")),
   url(r'^categorie/etc$', ListView.as_view(queryset=Document.objects.all().order_by("id"),template_name="acte/categorie.html")),
   url(r'^categorie/firma$', ListView.as_view(queryset=Document.objects.all().order_by("id"),template_name="acte/categorie.html")),
   url(r'^categorie/identitate$', ListView.as_view(queryset=Document.objects.all().order_by("id"),template_name="acte/categorie.html")),
   url(r'^categorie/imobiliar$', ListView.as_view(queryset=Document.objects.all().order_by("id"),template_name="acte/categorie.html")),
   url(r'^categorie/social$', ListView.as_view(queryset=Document.objects.all().order_by("id"),template_name="acte/categorie.html")),
   url(r'^categorie/medical$', ListView.as_view(queryset=Document.objects.all().order_by("id"),template_name="acte/categorie.html")),
   url(r'^contact$', views.contact, name = 'contact'),


## !! UPDATE THE TEMPLATES
# Add the rest of the URLs
   ]
