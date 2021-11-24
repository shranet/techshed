# Generated by Django 3.2.9 on 2021-11-24 20:30

from django.db import migrations, models
import techshed.validators


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(max_length=16, validators=[techshed.validators.PhoneValidator()]),
        ),
    ]
