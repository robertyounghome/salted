from django import forms
from .models import Account, Category
   
# creating a form 
class AccountForm(forms.Form):
    # class Meta:
    #     model = Account
    #     fields = ('name', 'site', 'html', 'username', 'password', 'category')

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    name = forms.CharField(max_length=50)
    site = forms.CharField(max_length=30)
    html = forms.CharField(max_length=100)
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget = forms.PasswordInput(), max_length=50)
