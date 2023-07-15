# Generated by Django 3.2.12 on 2023-07-13 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscricao', '0015_auto_20220810_1735'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artistas',
            options={'ordering': ['edicao', 'fliq', 'nome'], 'verbose_name': 'Artista', 'verbose_name_plural': 'Artistas'},
        ),
        migrations.AlterModelOptions(
            name='cosplay',
            options={'ordering': ['edicao', 'nome', 'personagem'], 'verbose_name': 'Cosplay', 'verbose_name_plural': 'Cosplays'},
        ),
        migrations.AlterModelOptions(
            name='cospobre',
            options={'ordering': ['edicao', 'nome', 'personagem'], 'verbose_name': 'Cospobre', 'verbose_name_plural': 'Cospobres'},
        ),
        migrations.AlterModelOptions(
            name='inscritos',
            options={'ordering': ['edicao', 'nome'], 'verbose_name': 'Participante', 'verbose_name_plural': 'Participantes'},
        ),
        migrations.AddField(
            model_name='cosplay',
            name='total_nota',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='cospobre',
            name='total_nota',
            field=models.IntegerField(default=0, null=True),
        ),
    ]