# Generated by Django 3.2.12 on 2022-06-29 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inscricao', '0008_artistas'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='edicao',
            options={'ordering': ['numero'], 'verbose_name': 'Edição', 'verbose_name_plural': 'Edições'},
        ),
    ]
