from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404, render
from django.template import RequestContext
from django.views.generic import TemplateView
from .models import Account, Category
from .forms import AccountForm, CategoryForm
from django.http import HttpResponseRedirect
import salted.encryption as E
from django.core.paginator import Paginator
from django.urls import reverse 

def is_correct_user(request):
    # account = Account.objects.all.get(pk=account_id)
    # return account and account.user == request.user
    return True

def add_to_context(request):  
    user = request.user
    name = user.first_name
    return {
        'user': user,
        'name': name,
    }

@login_required(login_url='login')
def index(request):
    context = {}
    try:
        accounts = Account.objects.filter(user = request.user.id).order_by('category', 'name')
    except Account.DoesNotExist:
        accounts = None
    paginator = Paginator(accounts, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context['page_obj'] = page_obj
    context['accounts'] = accounts
    c = RequestContext(request, processors=[add_to_context])
    return render(request, 'index.html', context)

def category_index(request):
    try:
        categories = Category.objects.filter(user = request.user.id)
    except Category.DoesNotExist:
        categories = None
    return render(request, "category_index.html", {'categories': categories}) 

def category_detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    if category.user != request.user:
        return HttpResponseRedirect(reverse("login"))
    if request.method == 'POST':
        form = CategoryForm(request.POST, user=request.user)
        if form.is_valid():
            category.name = form.cleaned_data['name']
            category.user = request.user
            category.save()
            return HttpResponseRedirect("/thanks/")
    else:
        context = {}
        context['form']= CategoryForm(page_name="Edit a Category", instance=category, user=request.user)
        context['category'] = category
        return render(request, 'new.html', context)

def category_new(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, user=request.user)
        if form.is_valid():
            category = Category(name=form.cleaned_data['name'],
                user=request.user)
            category.save()
            return HttpResponseRedirect("/thanks/")
    else:
        context ={}
        context['form']= CategoryForm(page_name="Add a Category", user=request.user)
        return render(request, 'new.html', context)   

def category_delete(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    if category.user != request.user:
        return HttpResponseRedirect("/accounts/login/")
    category.delete()
    return render(request, 'thanks.html', {})

@login_required(login_url='login')
# @user_passes_test(lambda request: is_correct_user, login_url="login")
def detail(request, account_id):
    account = get_object_or_404(Account, pk=account_id)
    if account.user != request.user:
        return HttpResponseRedirect("/accounts/login/")
    password = E.decrypt(account.password)
    context = {}
    context['form'] = AccountForm(page_name="View a Login", instance=account, password=password, user=request.user)
    context['account'] = account
    return render(request, 'new.html', context)

def new(request):
    if request.method == 'POST':
        form = AccountForm(request.POST, password=request.POST.get('password'), user=request.user)
        if form.is_valid():
            # cleaned_data = super(form, self).clean()
            encrypted_password = E.encrypt(form.cleaned_data['password'])
            # c = Category.objects.get(id=form.cleaned_data['category'])
            account = Account(name=form.cleaned_data['name'], 
                site=form.cleaned_data['site'], 
                html=form.cleaned_data['html'], 
                username=form.cleaned_data['username'],
                password=encrypted_password, user=request.user, 
                category=form.cleaned_data['category'])
            account.save()
            return HttpResponseRedirect("/thanks/")
    else:
        context ={}
        context['form']= AccountForm(page_name="Create a Login", user=request.user)
        return render(request, 'new.html', context)

def edit(request, account_id):
    account = get_object_or_404(Account, pk=account_id)
    if account.user != request.user:
        return HttpResponseRedirect("/accounts/login/")
    if request.method == 'POST':
        form = AccountForm(request.POST, password=request.POST.get('password'), user=request.user)
        if form.is_valid():
            encrypted_password = E.encrypt(form.cleaned_data['password'])
            account.name=form.cleaned_data['name']
            account.site=form.cleaned_data['site']
            account.html=form.cleaned_data['html']
            account.username=form.cleaned_data['username']
            account.password=encrypted_password
            account.category=form.cleaned_data['category']
            account.save()
            return HttpResponseRedirect("/thanks/")
    else:
        password = E.decrypt(account.password)
        # return render(request, 'edit.html', {'account': account})
        context ={}
        context['form']= AccountForm(page_name="Edit a Login", 
            instance=account, password=password, user=request.user)
        context['account'] = account
        return render(request, 'new.html', context)

def delete(request, account_id):
    account = get_object_or_404(Account, pk=account_id)
    if account.user != request.user:
        return HttpResponseRedirect("/accounts/login/")
    account.delete()
    return render(request, 'thanks.html', {})

def thanks(request):
    return render(request, 'thanks.html', {})

class AboutView(TemplateView):
    template_name = 'about.html'



