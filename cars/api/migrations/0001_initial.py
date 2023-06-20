# Generated by Django 4.2.2 on 2023-06-19 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='car_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('year_of_registration', models.DateField()),
                ('number_of_owners', models.IntegerField()),
                ('total_km', models.IntegerField()),
                ('fuel_type', models.CharField(choices=[('petrol', 'Petrol'), ('diesel', 'Diesel'), ('electric', 'Electric')], max_length=10)),
                ('car_image', models.ImageField(upload_to='')),
                ('car_video', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
