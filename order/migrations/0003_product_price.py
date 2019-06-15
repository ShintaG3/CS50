# Generated by Django 2.0.3 on 2019-05-18 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=39.99, max_digits=4),
        ),
    ]