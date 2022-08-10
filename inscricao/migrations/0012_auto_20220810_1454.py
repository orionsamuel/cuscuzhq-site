# Generated by Django 3.2.12 on 2022-08-10 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inscricao', '0011_auto_20220810_1448'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artistas',
            options={'ordering': ['nome', 'edicao', 'fliq'], 'verbose_name': 'Artista', 'verbose_name_plural': 'Artistas'},
        ),
        migrations.AddField(
            model_name='artistas',
            name='fliq',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='cosplay',
            name='edicao',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='inscricao.edicao'),
        ),
        migrations.DeleteModel(
            name='Fliq',
        ),
    ]
