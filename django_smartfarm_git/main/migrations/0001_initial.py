# Generated by Django 2.0.13 on 2020-08-23 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Good',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('good_min_temp', models.FloatField()),
                ('good_max_temp', models.FloatField(default=None)),
                ('good_min_humid', models.FloatField()),
                ('good_max_humid', models.FloatField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Month_Season',
            fields=[
                ('id', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('s_name', models.CharField(max_length=20)),
                ('s_min_month', models.IntegerField()),
                ('s_max_month', models.IntegerField()),
                ('s_season', models.CharField(default='', max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Other',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('good_min_temp', models.FloatField()),
                ('good_max_temp', models.FloatField(default=None)),
                ('good_min_humid', models.FloatField()),
                ('good_max_humid', models.FloatField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Temp',
            fields=[
                ('id', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('temper', models.IntegerField()),
                ('humadi', models.IntegerField()),
            ],
        ),
    ]
