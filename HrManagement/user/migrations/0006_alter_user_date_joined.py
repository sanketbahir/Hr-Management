# Generated by Django 3.2.19 on 2024-12-20 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_rename_user_name_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateField(auto_now_add=True),
        ),
    ]
