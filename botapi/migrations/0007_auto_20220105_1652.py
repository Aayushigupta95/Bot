# Generated by Django 3.2.5 on 2022-01-05 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botapi', '0006_auto_20220105_1648'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accountmanager',
            name='contact_no',
        ),
        migrations.AddField(
            model_name='finalaccountmanager',
            name='contact_no',
            field=models.CharField(max_length=12, null=True),
        ),
    ]