# Generated by Django 3.2.8 on 2021-10-28 15:18

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('cakesite', '0013_order_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(help_text='+79991234567', max_length=20, region=None, verbose_name='Номер телефона'),
        ),
    ]
