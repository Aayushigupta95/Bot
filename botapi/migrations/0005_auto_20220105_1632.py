# Generated by Django 3.2.5 on 2022-01-05 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('botapi', '0004_auto_20220105_1617'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accountmanager',
            old_name='name',
            new_name='accountmanager_name',
        ),
        migrations.AlterField(
            model_name='usermanager',
            name='manager_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='botapi.accountmanager'),
        ),
        migrations.DeleteModel(
            name='FinalAccountmanager',
        ),
    ]
