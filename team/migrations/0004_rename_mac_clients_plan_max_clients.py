# Generated by Django 4.2.2 on 2023-08-28 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0003_team_plan'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plan',
            old_name='mac_clients',
            new_name='max_clients',
        ),
    ]