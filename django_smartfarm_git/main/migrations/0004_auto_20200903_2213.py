# Generated by Django 2.0.13 on 2020-09-03 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200903_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='good_max_humid',
            field=models.FloatField(default='1970-01-01'),
        ),
    ]
