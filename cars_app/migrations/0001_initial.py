# Generated by Django 4.2.5 on 2023-10-03 00:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_name', models.CharField(max_length=255)),
                ('street_number', models.CharField(max_length=255)),
                ('zip_code', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('account_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cars_app.appuser')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_owners', models.IntegerField(default=0)),
                ('registration_number', models.CharField(max_length=255)),
                ('manufacture_year', models.IntegerField()),
                ('number_of_doors', models.IntegerField()),
                ('mileage', models.IntegerField()),
                ('car_model_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars_app.carmodel')),
            ],
        ),
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advertisement_date', models.DateTimeField()),
                ('car_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars_app.car')),
                ('seller_account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars_app.appuser')),
            ],
        ),
    ]
