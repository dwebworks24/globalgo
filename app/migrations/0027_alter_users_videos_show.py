# Generated by Django 5.0.7 on 2024-09-02 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_visaapplication_doc_1_visaapplication_doc_2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='videos_show',
            field=models.BooleanField(choices=[(True, 'Visible'), (False, 'Hidden')], default=False),
        ),
    ]
