# Generated by Django 5.1.7 on 2025-03-19 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0002_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='restuarant_type',
            field=models.CharField(choices=[('IN', 'Indian'), ('CH', 'Chinese'), ('IT', 'Italian'), ('GK', 'Greek'), ('MX', 'Mexican'), ('FF', 'Fast Food'), ('OT', 'Other')], default='', max_length=2),
            preserve_default=False,
        ),
    ]
