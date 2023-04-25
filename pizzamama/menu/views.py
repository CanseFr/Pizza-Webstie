from django.shortcuts import render
from django.http import HttpResponse 
from django.core import serializers # importer cette bibli pour l'api *-*
from .models import Pizza

# Create your views here.
def index(request):
    # V LIRE OBJET DE LA BASE DE données
    # # Recuperer objet pizza
    # pizzas = Pizza.objects.all()
    # # Recuperer Nom des pizza et prix
    # pizzas_names_price = [pizza.nom +" : "+ str(pizza.prix) +"€" for pizza in pizzas] 
    # pizzas_names_price_str = ", ".join(pizzas_names_price) 

    # # Retour affichage http
    # return HttpResponse("Les Pizzas : " + pizzas_names_price_str + " : €")
    
    # Suite 2) creer template
    pizzas = Pizza.objects.all() # je fais ma boucle de parcour dans le index.html
    #pizzas = Pizza.objects.all().order_by('prix') # si je souhaite les tier dans l'ordre de prix par exemple

    return render(request,'menu/index.html', {'pizzas' : pizzas} ) # Chemin vers mapage html


#Creation API *-*
def api_get_pizzas(request):
    pizzas = Pizza.objects.all()
    json = serializers.serialize("json", pizzas) # pour formater mes pizza au format json
    return HttpResponse(json)

