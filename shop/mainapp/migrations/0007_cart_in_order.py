# Generated by Django 3.1.2 on 2020-10-27 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_remove_cart_in_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='in_order',
            field=models.BooleanField(default=True),
        ),
    ]
