from django.shortcuts import render
from django.http import HttpResponse
from .models import Document

def index(request):
    return render(request, 'acte/home.html')

def contact(request):
    return render(request, 'acte/contact.html')

def search(request):
    q = request.GET['q']
    q = q.lower()
    object_list = Document.objects.order_by('name')
    context = {'object_list': object_list, 'q': q}
    return render(request, 'acte/search_results.html', context)
