# Generated by Django 3.2.12 on 2022-06-21 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inscricao', '0002_alter_inscritos_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cospobre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('telefone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=150)),
                ('imagem', models.ImageField(blank=True, upload_to='cospobre/images', verbose_name='Imagem')),
                ('som', models.FileField(blank=True, null=True, upload_to='cospobre/sounds', verbose_name='Musica')),
                ('nota_1', models.IntegerField(default=0, null=True)),
                ('edicao', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='inscricao.edicao')),
            ],
            options={
                'verbose_name': 'Participante',
                'verbose_name_plural': 'Participantes',
                'ordering': ['nome', 'edicao'],
            },
        ),
    ]
