# Generated by Django 5.0.2 on 2024-03-24 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_visatypes_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='Description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
