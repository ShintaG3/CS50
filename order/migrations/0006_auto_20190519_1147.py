# Generated by Django 2.0.3 on 2019-05-19 08:47

from django.db import migrations, models
import order.models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_auto_20190519_0809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=order.models.upload_image_path),
        ),
    ]
