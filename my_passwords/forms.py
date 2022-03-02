from unittest.util import _MAX_LENGTH
from django import forms
from .models import Account, Category
   
# creating a form 
# class AccountForm(forms.Form):
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit

class AccountForm(forms.ModelForm):
    def __init__(self, page_name, *args, **kwargs):
        password = kwargs.pop('password', None)
        super().__init__(*args, **kwargs)

        # Work around to make password editable since it is a non-editable BinaryField
        self.fields['password'] = forms.CharField(initial=password, required=True, max_length=50)
        
        if page_name == 'View a Login':
            self.fields['name'].disabled = True
            self.fields['site'].disabled = True 
            self.fields['html'].disabled = True 
            self.fields['username'].disabled = True 
            self.fields['password'].disabled = True 
            self.fields['category'].disabled = True

        self.helper = FormHelper(self)

        self.helper.form_id = 'id-accountForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = ''

        # self.helper.add_input(Submit('submit', 'Submit'))

        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'

        if page_name == 'View a Login':
            self.helper.layout = Layout(Fieldset(
                page_name,
                'name',
                'site',
                'html',
                'username',
                'password',
                'category'
            ))
        else:
            self.helper.layout = Layout(Fieldset(
                page_name,
                'name',
                'site',
                'html',
                'username',
                'password',
                'category'
            ),
            ButtonHolder(
                Submit('submit', 'Submit', css_class='button white')
            ))     

    def getCategories():
        return ((x.id, x.name) for x in Category.objects.all())

    # name = forms.CharField(max_length=50)
    # site = forms.CharField(max_length=30)
    # html = forms.CharField(max_length=100)
    # username = forms.CharField(max_length=50)
    # password = forms.CharField(widget = forms.PasswordInput(),
    #     max_length=50)
    # password_confirmation = forms.CharField(widget=forms.PasswordInput(), 
    #     max_length=50)
    # category = forms.CharField(widget = forms.Select(choices=getCategories()), 
    #     max_length=50)

    class Meta:
        model = Account
        fields = (
            'name',
            'site',
            'html',
            'username',
            'category'
        )

class CategoryForm(forms.Form):
    name = forms.CharField(max_length=50)
