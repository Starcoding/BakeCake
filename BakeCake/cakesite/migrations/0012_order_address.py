# Generated by Django 3.2.8 on 2021-10-27 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cakesite', '0011_auto_20211027_2252'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default='', max_length=120, verbose_name='адрес доставки'),
            preserve_default=False,
        ),
    ]
