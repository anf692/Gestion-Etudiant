# Generated by Django 5.1.5 on 2025-03-06 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etudiant', '0002_etudiant_profil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etudiant',
            name='profil',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
