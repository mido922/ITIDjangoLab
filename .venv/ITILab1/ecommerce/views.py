from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def homePage(request):
    template=loader.get_template('productList.html')
    context = {
    'products': [
      {
        'ID': '1',
        'Name': 'Galaxy Phone',
        'Description': 'A phone made by Samsung.',
      },
      {
        'ID': '2',
        'Name': 'SMP500 Laptop',
        'Description': 'The laptop for investors on a budget.',
      },
      {
        'ID': '3',
        'Name': 'Galaxy Tab 7',
        'Description': 'Samsung\'s newest iteration of the galaxy tab!',
      }]
    }
    return HttpResponse(template.render(context, request))

def category(request):
    template=loader.get_template('productListCategories.html')
    context = {
    'products': [
      {
        'ID': '1',
        'Name': 'Galaxy Phone',
        'Description': 'A phone made by Samsung.',
        'Category':'Phone',
      },
      {
        'ID': '2',
        'Name': 'SMP500 Laptop',
        'Description': 'The laptop for investors on a budget.',
        'Category':'Laptop'
      },
      {
        'ID': '3',
        'Name': 'Galaxy Tab 7',
        'Description': 'Samsung\'s newest iteration of the galaxy tab!',
        'Category':'Tablet',
      }]
    }
    return HttpResponse(template.render(context, request))

def aboutUs(request):
    template=loader.get_template('aboutUs.html')
    return HttpResponse(template.render({}, request))