# Generated by Django 2.0.3 on 2019-06-05 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0005_auto_20190605_0822'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='update',
        ),
    ]