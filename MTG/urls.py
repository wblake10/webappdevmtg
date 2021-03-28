from django.contrib import admin, auth
from django.urls import path, include
from mtg_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('home',views.home,name="home"),
    path('',views.entry,name="entry"),
    path('card_search',views.card_search,name="card_search"),
    path('search_results',views.search_results,name="search_results"),
    path('maintenance',views.maintenance,name="maintenance"),
    path('register', views.register_new_user, name="register_user"),
]