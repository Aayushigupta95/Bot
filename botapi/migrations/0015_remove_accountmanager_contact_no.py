# Generated by Django 3.2.5 on 2022-01-06 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('botapi', '0014_auto_20220106_1326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accountmanager',
            name='contact_no',
        ),
    ]