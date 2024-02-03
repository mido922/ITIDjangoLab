from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

products=[
      {
        'ID': 1,
        'Name': 'Galaxy Phone',
        'Description': 'A phone made by Samsung.',
        'Category':'Phone',
        'Source':'download.png',
      },
      {
        'ID': 2,
        'Name': 'SMP500 Laptop',
        'Description': 'The laptop for investors on a budget.',
        'Category':'Laptop',
        'Source':'download.png',
      },
      {
        'ID': 3,
        'Name': 'Galaxy Tab 7',
        'Description': 'Samsungs newest iteration of the galaxy tab!',
        'Category':'Tablet',
        'Source':'download.png',
      }
]

def homePage(request):
    context = {}
    context['products']=products
    return render(request, 'productList.html', context)

def category(request):
    context = {}
    context['products']=products
    return render(request, 'productListCategories.html', context)

def aboutUs(request):
    context = {}
    return render(request, 'aboutUs.html', context)

def productDetails(request, productID):
    context = {}
    context['products']=products
    
    track=filter(lambda t:t['ID']==productID,products)
    track=list(track)
    return HttpResponse(track)
    return render(request, 'productDetails.html', track)