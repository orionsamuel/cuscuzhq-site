# Generated by Django 4.0.5 on 2024-07-07 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscricao', '0019_auto_20230717_0055'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inscritos',
            old_name='presente',
            new_name='presente1',
        ),
        migrations.AddField(
            model_name='inscritos',
            name='presente2',
            field=models.BooleanField(default=False),
        ),
    ]