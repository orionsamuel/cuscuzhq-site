# Generated by Django 3.2.12 on 2023-07-17 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscricao', '0018_auto_20230715_0202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notascosplay',
            name='nota_1',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='notascosplay',
            name='nota_2',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='notascosplay',
            name='nota_3',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='notascosplay',
            name='total_nota',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='notascospobre',
            name='nota_1',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='notascospobre',
            name='nota_2',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='notascospobre',
            name='nota_3',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='notascospobre',
            name='total_nota',
            field=models.FloatField(default=0.0, null=True),
        ),
    ]