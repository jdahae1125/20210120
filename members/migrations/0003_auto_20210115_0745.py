# Generated by Django 3.1.5 on 2021-01-15 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_members_created'),
    ]

    operations = [
        migrations.RenameField(
            model_name='members',
            old_name='created',
            new_name='update',
        ),
    ]
