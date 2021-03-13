from django.shortcuts import render

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