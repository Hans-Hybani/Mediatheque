# Generated by Django 5.0.1 on 2024-02-19 10:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membre', '0004_delete_emprunteur_alter_cd_id_alter_dvd_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='emprunteur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=45)),
                ('bloque', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='cd',
            name='emprunteur_nom',
        ),
        migrations.RemoveField(
            model_name='dvd',
            name='emprunteur_nom',
        ),
        migrations.RemoveField(
            model_name='livre',
            name='emprunteur_nom',
        ),
        migrations.AddField(
            model_name='cd',
            name='emprunteur',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='membre.emprunteur'),
        ),
        migrations.AddField(
            model_name='dvd',
            name='emprunteur',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='membre.emprunteur'),
        ),
        migrations.AddField(
            model_name='jeudeplateau',
            name='emprunteur',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='membre.emprunteur'),
        ),
        migrations.AddField(
            model_name='livre',
            name='emprunteur',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='membre.emprunteur'),
        ),
    ]
