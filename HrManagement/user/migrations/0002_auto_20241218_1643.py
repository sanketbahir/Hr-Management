# Generated by Django 3.2.19 on 2024-12-18 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('Admin', 'admin'), ('employee', 'employee')], max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(choices=[('Admin', 'admin'), ('employee', 'employee')], max_length=50),
        ),
    ]
