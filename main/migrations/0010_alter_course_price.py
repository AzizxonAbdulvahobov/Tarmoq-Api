# Generated by Django 5.0.6 on 2024-06-14 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='price',
            field=models.FloatField(help_text='One month course price'),
        ),
    ]
