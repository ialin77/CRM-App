# Generated by Django 4.2.2 on 2023-08-29 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0005_clientfile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientfile',
            old_name='lead',
            new_name='client',
        ),
    ]
