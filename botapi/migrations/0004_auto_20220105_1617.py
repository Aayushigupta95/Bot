# Generated by Django 3.2.5 on 2022-01-05 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('botapi', '0003_rename_name_accountmanager_accountmanager_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accountmanager',
            old_name='accountmanager_name',
            new_name='name',
        ),
        migrations.CreateModel(
            name='FinalAccountmanager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accountmanager_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='botapi.accountmanager')),
            ],
        ),
        migrations.AlterField(
            model_name='usermanager',
            name='manager_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='botapi.finalaccountmanager'),
        ),
    ]
