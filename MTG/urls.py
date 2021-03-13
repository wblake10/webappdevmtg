from django.contrib import admin
from django.urls import path
from mtg_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('card_search',views.card_search,name="card_search"),
    path('search_results',views.search_results,name="search_results"),
    path('maintenance',views.maintenance,name="maintenance"),
]