# Generated by Django 3.1.7 on 2021-05-17 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20210516_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='input',
            name='first_line',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='input',
            name='style',
            field=models.CharField(choices=[('Machine', 'Machine'), ('Shakespeare', 'Shakespeare'), ('Ginsberg', 'Ginsberg'), ('Cummings', 'Cummings'), ('Lorem Ipsum', 'Lorem Ipsum')], default=('Machine', 'Machine'), max_length=100),
        ),
        migrations.AlterField(
            model_name='poem',
            name='author',
            field=models.CharField(choices=[('Machine', 'Machine'), ('Shakespeare', 'Shakespeare'), ('Ginsberg', 'Ginsberg'), ('Cummings', 'Cummings'), ('Lorem Ipsum', 'Lorem Ipsum')], default=('Machine', 'Machine'), max_length=100),
        ),
    ]
