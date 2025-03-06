from django import forms
from django.forms import ModelForm
from .models import Etudiant

class AjoutForm(forms.ModelForm):
    
    class Meta:
        model = Etudiant
        fields =['prenom','nom','age','metier','est_inscrit']
        widget={
           'nom': forms.TextInput(
               attrs={'class': 'form-control', 'placeholder': 'Entrez votre nom'}
               ),

            'prenom': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Entrez votre prénom'}
                ),

            'age': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Entrez votre âge'}
                ),

            'metier': forms.Select(
                attrs={'class': 'form-control'}
                ),  # Assurez-vous que le modèle a bien le champ choices

            'est_inscrit': forms.CheckboxInput(
                attrs={'class': 'form-check-input'}
                ),
        }
        