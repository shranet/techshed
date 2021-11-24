# Generated by Django 3.2.9 on 2021-11-24 20:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import techshed.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0006_product_available'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('phone', models.TextField(max_length=16, validators=[techshed.validators.PhoneValidator()])),
                ('zip_code', models.CharField(max_length=20)),
                ('status', models.SmallIntegerField(choices=[(0, 'New'), (1, 'Accepted'), (2, 'Rejected'), (3, 'In delivery'), (4, 'Delivered'), (5, 'Closed')])),
                ('payment_status', models.SmallIntegerField(choices=[(0, 'New'), (3, 'Rejected'), (2, 'Complete'), (1, 'Prepare')], default=0)),
                ('order_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='cart.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='main.product')),
            ],
        ),
    ]