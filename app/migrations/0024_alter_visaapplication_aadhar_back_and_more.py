# Generated by Django 4.1.2 on 2024-08-26 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_users_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visaapplication',
            name='aadhar_back',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='visaapplication',
            name='aadhar_front',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='visaapplication',
            name='upload_passport_back',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='visaapplication',
            name='upload_passport_front',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]