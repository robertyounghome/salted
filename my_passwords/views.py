from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.template import RequestContext
from django.views.generic import TemplateView
from .models import Account, Category
from .forms import AccountForm, CategoryForm
from django.http import HttpResponseRedirect
from django.template import RequestContext
import salted.encryption as E

# RequestContext(request, {'message': 'I am the second view.'},
#             processors=[custom_proc])

def add_to_context(request):  
    user = request.user
    name = user.first_name
    return {
        'user': user,
        'name': name,
    }

@login_required(login_url='login')
def index(request):
    try:
        accounts = Account.objects.filter(user = request.user.id)
    except Account.DoesNotExist:
        accounts = None
    c = RequestContext(request,processors=[add_to_context])
    return render(request, 'index.html', {'accounts': accounts})

def category_index(request):
    try:
        categories = Category.objects.filter(user = request.user.id)
    except Category.DoesNotExist:
        categories = None
    return render(request, 'category_index.html', {'categories': categories}) 

def category_detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    return render(request, 'category_detail.html', {'category': category})

def category_new(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = Category(name=form.cleaned_data['name'])
            category.save()
            return HttpResponseRedirect("/thanks/")
    else:
        context ={}
        context['form']= CategoryForm()
        return render(request, 'category_new.html', context)   

def detail(request, account_id):
    account = get_object_or_404(Account, pk=account_id)
    account.password = E.decrypt(account.password)
    return render(request, 'detail.html', {'account': account})

def new(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            encrypted_password = E.encrypt(form.cleaned_data['password'])
            c = Category.objects.get(id=form.cleaned_data['category'])
            account = Account(name=form.cleaned_data['name'], 
                site=form.cleaned_data['site'], 
                html=form.cleaned_data['html'], 
                username=form.cleaned_data['username'],
                password=encrypted_password, user=request.user, 
                category=c)
            account.save()
            return HttpResponseRedirect("/thanks/")
    else:
        context ={}
        context['form']= AccountForm()
        return render(request, 'new.html', context)

def edit(request, account_id):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            encrypted_password = E.encrypt(form.cleaned_data['password'])
            c = Category.objects.get(id=form.cleaned_data['category'])
            account = Account(name=form.cleaned_data['name'], 
                site=form.cleaned_data['site'], 
                html=form.cleaned_data['html'], 
                username=form.cleaned_data['username'],
                password=encrypted_password, user=request.user, 
                category=c)
            account.save()
            return HttpResponseRedirect("/thanks/")
    else:
        account = get_object_or_404(Account, pk=account_id)
        account.password = E.decrypt(account.password)
        # return render(request, 'edit.html', {'account': account})
        context ={}
        context['form']= AccountForm()
        context['account'] = account
        return render(request, 'edit.html', context)

def thanks(request):
    return render(request, 'thanks.html', {})

class AboutView(TemplateView):
    template_name = 'about.html'



