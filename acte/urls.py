from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from acte.models import Document, Institution
from . import views

urlpatterns = [
   url(r'^$' , views.index , name ='index'),
   url(r'^documente$', ListView.as_view(queryset=Document.objects.all().order_by("id"),template_name="acte/lista_acte.html")),
   url(r'^documente/(?P<pk>\d+)$', DetailView.as_view(model = Document, template_name="acte/act.html")),
   url(r'^institutii$', ListView.as_view(queryset=Institution.objects.all().order_by("id"),template_name="acte/lista_institutii.html")),
   url(r'^institutii/(?P<pk>\d+)$', DetailView.as_view(model = Institution, template_name="acte/institutie.html")),
   url(r'^categorie/(?P<pk>\d+)$', ListView.as_view(queryset=Document.objects.all().order_by("id"),template_name="acte/categorie.html")),
   url(r'^contact$', views.contact, name = 'contact'),


## !! UPDATE THE TEMPLATES
# Add the rest of the URLs
   ]
