# Generated by Django 4.1 on 2022-08-27 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='productoPrecio',
            field=models.FloatField(default=0.0),
        ),
    ]