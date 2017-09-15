from django.shortcuts import render
from django.http import HttpResponse
from .models import Document

def index(request):
    return render(request, 'acte/home.html')

def contact(request):
    return render(request, 'acte/contact.html')

def search(request):
    q = request.GET['q']
    object_list = Document.objects.filter(name=q).order_by('name')
    print(object_list)
    context = {'object_list': object_list}
    return render(request, 'acte/search_results.html', context)
