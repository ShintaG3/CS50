# Generated by Django 2.0.3 on 2019-06-06 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0009_auto_20190606_2321'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='unit_price',
            field=models.DecimalField(decimal_places=2, default=10.99, max_digits=1000),
        ),
    ]