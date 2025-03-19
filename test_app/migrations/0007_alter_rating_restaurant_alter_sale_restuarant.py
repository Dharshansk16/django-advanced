# Generated by Django 5.1.7 on 2025-03-19 10:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0006_rename_restuarant_type_restaurant_restaurant_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating', to='test_app.restaurant'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='restuarant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sale', to='test_app.restaurant'),
        ),
    ]
