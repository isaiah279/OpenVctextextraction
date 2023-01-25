# Generated by Django 4.0.6 on 2023-01-19 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trackerApp', '0003_drugsmodels_description2_drugsmodels_description3'),
    ]

    operations = [
        migrations.CreateModel(
            name='AerosalModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aerosalname', models.CharField(max_length=50)),
                ('aerosalpicture', models.ImageField(null=True, upload_to='')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('description1', models.TextField(max_length=70)),
                ('description2', models.CharField(max_length=100)),
                ('description3', models.CharField(max_length=105)),
            ],
        ),
        migrations.CreateModel(
            name='BreadModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breadname', models.CharField(max_length=50)),
                ('beardpicture', models.ImageField(null=True, upload_to='')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('description1', models.TextField(max_length=70)),
                ('description2', models.CharField(max_length=100)),
                ('description3', models.CharField(max_length=105)),
            ],
        ),
        migrations.CreateModel(
            name='SoaplModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soapname', models.CharField(max_length=50)),
                ('soappicture', models.ImageField(null=True, upload_to='')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('description1', models.TextField(max_length=70)),
                ('description2', models.CharField(max_length=100)),
                ('description3', models.CharField(max_length=105)),
            ],
        ),
    ]