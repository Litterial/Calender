# Generated by Django 2.0.6 on 2019-08-12 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=35)),
                ('lname', models.CharField(max_length=35)),
                ('address', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateField()),
                ('time', models.TimeField(choices=[('07:00:00', '7 AM'), ('08:00:00', '8 AM'), ('09:00:00', '9 AM'), ('10:00:00', '10 AM'), ('11:00:00', '11 AM'), ('12:00:00', '12 PM'), ('13:00:00', '1 AM'), ('14:00:00', '2 AM'), ('15:00:00', '3 AM'), ('16:00:00', '4 AM'), ('17:00:00', '5 AM')])),
            ],
        ),
    ]
