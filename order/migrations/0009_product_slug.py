# Generated by Django 2.0.3 on 2019-05-19 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_product_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='abc'),
        ),
    ]
