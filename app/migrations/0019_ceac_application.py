# Generated by Django 4.1.2 on 2024-07-03 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_pointofcontact_professional_experience'),
    ]

    operations = [
        migrations.CreateModel(
            name='ceac_application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('password', models.CharField(blank=True, max_length=100, null=True)),
                ('questio', models.CharField(max_length=255)),
                ('answer', models.CharField(max_length=255)),
                ('application_user', models.ForeignKey(db_column='visaApplication_id', on_delete=django.db.models.deletion.DO_NOTHING, to='app.visaapplication')),
            ],
            options={
                'db_table': 'ceac_application',
                'managed': True,
            },
        ),
    ]
