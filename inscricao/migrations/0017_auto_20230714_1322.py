# Generated by Django 3.2.12 on 2023-07-14 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inscricao', '0016_auto_20230713_0056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cosplay',
            name='nota_1',
        ),
        migrations.RemoveField(
            model_name='cosplay',
            name='nota_2',
        ),
        migrations.RemoveField(
            model_name='cosplay',
            name='nota_3',
        ),
        migrations.RemoveField(
            model_name='cosplay',
            name='total_nota',
        ),
        migrations.RemoveField(
            model_name='cospobre',
            name='nota_1',
        ),
        migrations.RemoveField(
            model_name='cospobre',
            name='nota_2',
        ),
        migrations.RemoveField(
            model_name='cospobre',
            name='nota_3',
        ),
        migrations.RemoveField(
            model_name='cospobre',
            name='total_nota',
        ),
        migrations.CreateModel(
            name='NotasCospobre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('personagem', models.CharField(max_length=150, null=True)),
                ('nota_1', models.IntegerField(default=0, null=True)),
                ('nota_2', models.IntegerField(default=0, null=True)),
                ('nota_3', models.IntegerField(default=0, null=True)),
                ('total_nota', models.IntegerField(default=0, null=True)),
                ('edicao', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='inscricao.edicao')),
            ],
            options={
                'verbose_name': 'Nota Cospobre',
                'verbose_name_plural': 'Notas Cospobres',
                'ordering': ['edicao', 'total_nota'],
            },
        ),
        migrations.CreateModel(
            name='NotasCosplay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('personagem', models.CharField(max_length=150, null=True)),
                ('nota_1', models.IntegerField(default=0, null=True)),
                ('nota_2', models.IntegerField(default=0, null=True)),
                ('nota_3', models.IntegerField(default=0, null=True)),
                ('total_nota', models.IntegerField(default=0, null=True)),
                ('edicao', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='inscricao.edicao')),
            ],
            options={
                'verbose_name': 'Nota Cosplay',
                'verbose_name_plural': 'Notas Cosplays',
                'ordering': ['edicao', 'total_nota'],
            },
        ),
    ]