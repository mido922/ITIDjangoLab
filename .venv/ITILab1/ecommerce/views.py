from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import *

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
    context = {'products': Product.objects.all()}
    return render(request, 'productList.html', context)

def category(request):
    context = {}
    context = {'products': Product.objects.all()}
    return render(request, 'productListCategories.html', context)

def aboutUs(request):
    context = {}
    return render(request, 'aboutUs.html', context)

def addNewProduct(request):
    if(request.method=="POST"):
        Product.objects.create(ID=request.POST['productID'],
                               Name=request.POST['productName'],
                               Description=request.POST['productDescription'],
                               Category=request.POST['productCategory'],
                               Image=request.POST['productImage'],)
        return HttpResponseRedirect('/')
    
    return render(request, 'addNewProduct.html')

def productDetails(request, productID):
  selectedProduct=Product.objects.get(ID=productID)
  context={'products':selectedProduct}
  return render(request, 'productDetails.html', context)

def deleteProduct(request,productID):
  Product.objects.filter(ID=productID).delete()
  return HttpResponseRedirect('/')

def updateProduct(request,productID):
  newProductDetails=Product.objects.get(ID=productID)
  context={'products':newProductDetails}
  if(request.method=="POST"):
      Product.objects.filter(id=productID).update(ID=request.POST['productID'],
                              Name=request.POST['productName'],
                              Description=request.POST['productDescription'],
                              Category=request.POST['productCategory'],
                              Image=request.POST['productImage'],)
      return HttpResponseRedirect('/')


  return render(request, 'updateProduct.html',)