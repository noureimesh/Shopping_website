# Generated by Django 3.2 on 2022-05-18 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='photo',
            field=models.ImageField(default='![](../products/default.jpg)', upload_to='products'),
        ),
    ]