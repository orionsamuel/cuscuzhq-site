# Generated by Django 3.2.12 on 2022-08-10 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscricao', '0014_alter_artistas_fliq'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artistas',
            name='fliq',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='artistas',
            name='obrasFuturas',
            field=models.TextField(blank=True, max_length=400),
        ),
    ]
