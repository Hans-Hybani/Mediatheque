# Generated by Django 5.0.1 on 2024-02-20 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliotecaire', '0007_remove_jeudeplateau_dateemprunt_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='emprunteur',
            name='nb_emprunts',
            field=models.IntegerField(default=0),
        ),
    ]
