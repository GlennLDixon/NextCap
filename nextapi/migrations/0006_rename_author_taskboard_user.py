# Generated by Django 4.1 on 2022-09-14 01:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nextapi', '0005_rename_user_taskboard_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taskboard',
            old_name='author',
            new_name='user',
        ),
    ]
