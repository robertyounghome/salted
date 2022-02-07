from unittest.util import _MAX_LENGTH
from django import forms
from .models import Account, Category
   
# creating a form 
# class AccountForm(forms.Form):
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit

class AccountForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        self.helper.form_id = 'id-accountForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = ''

        # self.helper.add_input(Submit('submit', 'Submit'))

        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(Fieldset(
            'New Login Creation',
            'name',
            'site',
            'html',
            'username',
            'password',
            'password_confirmation',
            'category',
        ),
        ButtonHolder(
            Submit('submit', 'Submit', css_class='button white')
        ))     
    def getCategories():
        return ((x.id, x.name) for x in Category.objects.all())

    name = forms.CharField(max_length=50)
    site = forms.CharField(max_length=30)
    html = forms.CharField(max_length=100)
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget = forms.PasswordInput(),
        max_length=50)
    password_confirmation = forms.CharField(widget=forms.PasswordInput(), 
        max_length=50)
    category = forms.CharField(widget = forms.Select(choices=getCategories()), 
        max_length=50)

class CategoryForm(forms.Form):
    name = forms.CharField(max_length=50)
