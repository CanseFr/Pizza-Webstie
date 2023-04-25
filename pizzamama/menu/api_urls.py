from django.urls import path
from . import views

# Fichier url pour l'api , eviter trop de slash dans la bar d'adresse
app_name = 'menu'

urlpatterns = [
    path('GetPizzas', views.api_get_pizzas), # url de notre API
    ]