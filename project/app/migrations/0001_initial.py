# Generated by Django 5.1.5 on 2025-03-24 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admindatabase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_name', models.CharField(max_length=50)),
                ('admin_email', models.EmailField(max_length=254)),
                ('date_of_joining', models.DateField()),
                ('contact_number', models.IntegerField()),
                ('admin_password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employe_name', models.CharField(max_length=50)),
                ('employe_email', models.EmailField(max_length=254)),
                ('employe_dob', models.DateField()),
                ('date_of_joining', models.DateField()),
                ('department', models.CharField(max_length=50)),
                ('contact_number', models.IntegerField()),
                ('employe_password', models.CharField(max_length=50)),
                ('your_work', models.CharField(max_length=100)),
            ],
        ),
    ]
