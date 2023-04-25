from django.db import models


# Models menu.
class Pizza(models.Model):
    nom = models.CharField(max_length=200) # nom est egale a une chaine de caractere dont le nombre de char doit etre specifié
    ingredients = models.CharField(max_length=400)
    prix = models.FloatField(default=0)
    vegetarienne = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nom
    
    
    
    