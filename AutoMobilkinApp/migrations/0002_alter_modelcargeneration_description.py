# Generated by Django 4.1.7 on 2023-02-24 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AutoMobilkinApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelcargeneration',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
