# Generated by Django 3.2.5 on 2022-01-06 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('botapi', '0009_alter_usermanager_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermanager',
            name='manager_name',
        ),
    ]