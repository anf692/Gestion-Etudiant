from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('details/<int:id>', details, name="details"),
    path('ajout/', ajout_etudiant, name="etudiants"),
    path('supprime/<int:id>', Supprimer_etudiant, name='supprimer'),
    path('modifier/<int:id>', modifier_etudiant, name='modifier'),
]