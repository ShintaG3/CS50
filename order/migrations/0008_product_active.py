# Generated by Django 2.0.3 on 2019-05-19 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_product_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]