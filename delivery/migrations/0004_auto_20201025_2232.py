# Generated by Django 3.1.1 on 2020-10-25 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0003_auto_20201025_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='deliverydate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
