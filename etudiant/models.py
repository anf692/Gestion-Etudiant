from django.db import models

# Create your models here.
class Etudiant(models.Model):
    METIER=[('APD','APD'),('DFE','DFE'),('FCA','FCA')]
    nom= models.CharField(max_length=20)
    prenom=models.CharField(max_length=20)
    age=models.PositiveIntegerField()
    metier=models.CharField(max_length=20, choices=METIER)
    est_inscrit=models.BooleanField()
    create_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"
