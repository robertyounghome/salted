from unittest.util import _MAX_LENGTH
from django import forms
from .models import Account, Category
   
# creating a form 
class AccountForm(forms.Form):
    # class Meta:
    #     model = Account
    #     fields = ('name', 'site', 'html', 'username', 'password', 'category')

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    c = []
    for x in Category.objects.all():
        c.append((x.id, x.name))
    name = forms.CharField(max_length=50)
    site = forms.CharField(max_length=30)
    html = forms.CharField(max_length=100)
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget = forms.PasswordInput(), max_length=50)
    category = forms.CharField(widget = forms.Select(choices=c), max_length=50)

class CategoryForm(forms.Form):
    name = forms.CharField(max_length=50)
