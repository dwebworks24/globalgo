# Generated by Django 4.1.2 on 2024-08-05 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_contact_alter_visatypes_visa_types'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='videos_show',
            field=models.BooleanField(choices=[(True, 'Visible'), (False, 'Hidden')], default=True),
        ),
        migrations.AlterModelTable(
            name='contact',
            table='Contact',
        ),
    ]