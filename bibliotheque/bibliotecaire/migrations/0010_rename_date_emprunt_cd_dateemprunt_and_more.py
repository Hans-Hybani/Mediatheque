# Generated by Django 5.0.1 on 2024-02-20 23:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bibliotecaire', '0009_rename_dateemprunt_cd_date_emprunt_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cd',
            old_name='date_emprunt',
            new_name='dateEmprunt',
        ),
        migrations.RenameField(
            model_name='dvd',
            old_name='date_emprunt',
            new_name='dateEmprunt',
        ),
        migrations.RenameField(
            model_name='livre',
            old_name='date_emprunt',
            new_name='dateEmprunt',
        ),
    ]
