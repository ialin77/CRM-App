# Generated by Django 4.2.2 on 2023-08-29 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_userprofile_active_team_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='active_team_id',
            new_name='active_team',
        ),
    ]
