# Generated by Django 4.0 on 2022-02-04 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Car', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('DateOfBirth', models.DateField()),
                ('accountCreated', models.DateField(auto_now=True)),
                ('contactInfo', models.CharField(max_length=14)),
                ('favouriteCar', models.ManyToManyField(to='Car.Car')),
            ],
        ),
    ]
