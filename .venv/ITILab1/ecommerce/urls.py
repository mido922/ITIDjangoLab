from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name = 'homePage'),
    path('category/', views.category, name = 'category'),
    path('aboutUs/', views.aboutUs, name= 'aboutUs')
]