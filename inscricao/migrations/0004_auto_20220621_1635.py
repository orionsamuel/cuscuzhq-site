# Generated by Django 3.2.12 on 2022-06-21 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscricao', '0003_cospobre'),
    ]

    operations = [
        migrations.AddField(
            model_name='cospobre',
            name='nota_2',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='cospobre',
            name='nota_3',
            field=models.IntegerField(default=0, null=True),
        ),
    ]