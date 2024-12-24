# Generated by Django 3.2.19 on 2024-12-18 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('female', 'female'), ('other', 'other')], max_length=10)),
                ('profile_pic', models.ImageField(upload_to='', verbose_name=models.ImageField(null=True, upload_to='profile_pics/'))),
                ('data_of_joining', models.DateField()),
                ('status', models.CharField(choices=[('active', 'active'), ('inactive', 'active')], max_length=10)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.department')),
            ],
        ),
    ]
