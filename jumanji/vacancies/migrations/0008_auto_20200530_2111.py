# Generated by Django 3.0.6 on 2020-05-30 21:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0007_auto_20200528_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='written_phone',
            field=models.PositiveIntegerField(
                validators=[
                    django.core.validators.MaxValueValidator(99999999999),
                    django.core.validators.MinValueValidator(10000000000)
                ]
            ),
        ),
    ]