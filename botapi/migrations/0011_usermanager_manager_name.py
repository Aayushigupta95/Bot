# Generated by Django 3.2.5 on 2022-01-06 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('botapi', '0010_remove_usermanager_manager_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermanager',
            name='manager_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='botapi.finalaccountmanager'),
        ),
    ]
