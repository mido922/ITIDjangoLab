from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import *
from .forms import *

# Create your views here.

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

def addNewProductForm(request):
    form=ProductForm()
    context={'form':form}
    if(request.method=="POST"):
       form=ProductForm(request, request.POST, request.FILES)
       if(form.is_valid()):
        Product.objects.create(ID=request.POST.get['productID'],
                               Name=request.POST.get['productName'],
                               Description=request.POST.get['productDescription'],
                               Category=request.POST.get['productCategory'],
                               Image=request.POST.get['productImage'],)
        return HttpResponseRedirect('/')
       else:
        return HttpResponseRedirect('/')
    return render(request, 'addNewProductForm.html', context)

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
                              Image=request.FILES['productImage'],)
      return HttpResponseRedirect('/')


  return render(request, 'updateProduct.html',)