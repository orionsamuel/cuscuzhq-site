# Generated by Django 3.2.12 on 2022-06-21 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inscricao', '0004_auto_20220621_1635'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cospobre',
            options={'ordering': ['nome', 'edicao'], 'verbose_name': 'Cospobre', 'verbose_name_plural': 'Cospobres'},
        ),
    ]
