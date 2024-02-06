from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name = 'homePage'),
    path('addNewProduct/', views.addNewProduct, name= 'addNewProduct'),
    path('category/', views.category, name = 'category'),
    path('aboutUs/', views.aboutUs, name = 'aboutUs'),
    path('products/<int:productID>', views.productDetails, name = 'productDetails'),
    path('deleteProduct/<int:productID>', views.deleteProduct, name = 'deleteProduct'),
    path('updateProduct/<int:productID>', views.updateProduct, name = 'updateProduct'),
]