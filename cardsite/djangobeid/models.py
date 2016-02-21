from django.db import models
import datetime

# Create your models here.

GENDER_CHOICES = (
    ('M', 'Homme'),
    ('F', 'Femme'),
)

class Personne(models.Model):

    num_nat = models.CharField("Numéro national", max_length=11, blank=True)
    nom = models.CharField(max_length=100)
    prenoms = models.CharField("Prénom(s)", max_length=100)
    date_naissance = models.DateField("Date de naissance", blank=True, null=True)
    lieu_naissance = models.CharField(max_length=100, blank=True)
    nationalite = models.CharField("Nationalité", max_length=100, blank=True)
    sexe = models.CharField(max_length=1, choices=GENDER_CHOICES)

    num_carte = models.CharField("Numéro de carte", max_length=100, blank=True)
    debut_val = models.DateField("Début de validité", blank=True, null=True)
    fin_val = models.DateField("Fin de validité", blank=True, null=True)
    commune_del = models.CharField("Commune de délivrance", max_length=100, blank=True)
    
    rue_et_num = models.CharField("Rue et numéro", max_length=200, blank=True)
    code_postal = models.CharField("Code postal", max_length=6, blank=True)
    commune = models.CharField(max_length=100, blank=True)
    
    photo = models.TextField("Photo")

    # Added to define access permissions
    acces_autorise = models.BooleanField("Accès autorisé", default=True)

    def __str__(self):
        return "%s %s" % (self.prenoms, self.nom)


    def card_is_valid(self):
        if self.fin_val:
            return (datetime.date.today() <= self.fin_val)
        else:
            return False    
    card_is_valid.short_description = "CI valide"
    card_is_valid.boolean = True
