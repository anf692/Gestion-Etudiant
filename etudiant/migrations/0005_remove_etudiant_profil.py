# Generated by Django 5.1.5 on 2025-03-06 22:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etudiant', '0004_alter_etudiant_profil'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='etudiant',
            name='profil',
        ),
    ]
