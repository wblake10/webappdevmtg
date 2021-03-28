from django.shortcuts import render
from mtg_app.models import AccountHolder
from django.contrib.auth.forms import UserCreationForm

# App homepage
def home(request):
    data = dict()
    return render(request, "home.html")

def card_search(request):
    data = dict()
    return render(request, "card_search.html")

def search_results(request):
    data = dict()
    return render(request, "search_results.html")

def maintenance(request):
    data = dict()
    return render(request, "maintenance.html")

def register_new_user(request):
    context = dict()
    form = UserCreationForm(request.POST)
    if form.is_valid():
        new_user = form.save()
        dob = request.POST["dob"]
        acct_holder = AccountHolder(user=new_user,date_of_birth=dob)
        acct_holder.save()
        return render(request,"home.html",context=dict())
    else:
        form = UserCreationForm()
        context['form'] = form
        return render(request, "registration/register.html", context)

def entry(request):
    data = dict()
    return render(request,"entry.html",context=data)

def login(request):
    data = dict()
    return render(request,"registration/login.html",context=data)