from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import *
from .forms import *

# Create your views here.

def homePage(request):
    context = {'products': Product.objects.all()}
    return render(request, 'productList.html', context)

def category(request):
    context = {'products': Product.objects.all()}
    return render(request, 'productListCategories.html', context)

def aboutUs(request):
    context = {}
    return render(request, 'aboutUs.html', context)

def addNewProduct(request):
    if(request.method=="POST"):
        Product.objects.create(Name=request.POST['productName'],
                               Description=request.POST['productDescription'],
                               Category=request.POST['productCategory'],
                               Image=request.POST['productImage'],)
        return HttpResponseRedirect('/')
    return render(request, 'addNewProduct.html')

def addNewProductForm(request):
    form=ProductForm()
    context={'form':form}
    if(request.method=="POST"):
       form=ProductForm(request.POST)
       if(form.is_valid()):
        Product.objects.create(Name=request.POST['productName'],
                               Description=request.POST['productDescription'],
                               Category=request.POST['productCategory'],)
        return HttpResponseRedirect('/')
       else:
        return HttpResponseRedirect('/')
    return render(request, 'addNewProductForm.html', context)

def productDetails(request, productID):
  selectedProduct=Product.objects.get(id=productID)
  context={'products':selectedProduct}
  return render(request, 'productDetails.html', context)

def deleteProduct(request,productID):
  Product.objects.filter(id=productID).delete()
  return HttpResponseRedirect('/')

def updateProduct(request,productID):
  newProductDetails=Product.objects.get(id=productID)
  context={'products':newProductDetails}
  if(request.method=="POST"):
      Product.objects.filter(id=productID).update(
                                Name=request.POST['productName'],
                                Description=request.POST['productDescription'],
                                Category=request.POST['productCategory'],
                                Image=request.FILES['productImage'],)
      return HttpResponseRedirect('/')

  return render(request, 'updateProduct.html',)