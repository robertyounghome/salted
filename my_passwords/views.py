from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.template import RequestContext
from django.views.generic import TemplateView
from .models import Account, Category
from .forms import AccountForm
from django.http import HttpResponseRedirect
import salted.encryption as E

@login_required(login_url='login')
def index(request):
    # context = RequestContext(request)
    try:
        accounts = Account.objects.filter(user = request.user.id)
    except Account.DoesNotExist:
        accounts = None
    return render(request, 'index.html', {'accounts': accounts})

def detail(request, account_id):
    account = get_object_or_404(Account, pk=account_id)
    account.password = E.decrypt(account.password)
    return render(request, 'detail.html', {'account': account})

def new(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            # process the data
            encrypted_password = E.encrypt(form.cleaned_data['password'])
            account = Account(name=form.cleaned_data['name'], 
                site=form.cleaned_data['site'], 
                html=form.cleaned_data['html'], 
                username=form.cleaned_data['username'],
                password=encrypted_password, user=request.user, 
                category=get_object_or_404(Category, id=1))
            account.save()
            return HttpResponseRedirect("/thanks/")
    else:
        context ={}
        context['form']= AccountForm()
        return render(request, 'new.html', context)

def thanks(request):
    return render(request, 'thanks.html', {})

class AboutView(TemplateView):
    template_name = 'about.html'



