# Generated by Django 2.0.3 on 2019-05-19 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='products/'),
        ),
    ]
