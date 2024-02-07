from django import forms

class ProductForm(forms.Form):
    productName = forms.CharField(max_length=30)
    productDescription = forms.CharField(max_length=50)
    productCategory = forms.CharField(max_length=10)