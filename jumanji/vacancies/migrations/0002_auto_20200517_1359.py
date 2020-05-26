# Generated by Django 3.0.6 on 2020-05-17 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='description',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='company',
            name='employee_count',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='location',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='description',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='skills',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]