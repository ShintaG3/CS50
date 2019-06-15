# Generated by Django 2.0.3 on 2019-05-19 05:09

from django.db import migrations, models
import order.models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=order.models.upload_image_path),
        ),
    ]