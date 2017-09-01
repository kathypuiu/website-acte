from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'acte/home.html')

def categorii(request):
    return render(request, 'acte/home.html')    #Update this one later
