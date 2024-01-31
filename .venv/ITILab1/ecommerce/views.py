from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def helloCU(request):
    return HttpResponse("Welcome to my ecommerce site.")
def aboutUs(request):
    return HttpResponse("This website made for ITI in Django.")