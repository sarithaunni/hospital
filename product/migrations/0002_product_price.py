# Generated by Django 3.0.2 on 2020-01-27 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=25),
            preserve_default=False,
        ),
    ]
