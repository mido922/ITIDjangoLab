from django import forms

class ProductForm(forms.Form):
    ID = forms.CharField(max_length=30, required=True)
    Name = forms.CharField(max_length=30)
    Description = forms.CharField(max_length=50)
    Category = forms.CharField(max_length=10)