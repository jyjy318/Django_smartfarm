from django.db import models

class Temp(models.Model):
    id = models.AutoField(primary_key=True,default=None)
    temper = models.IntegerField(null=False)
    humadi = models.IntegerField(null=False)

class Good(models.Model):
    name = models.CharField(max_length=20, primary_key=True, null=False)
    good_min_temp = models.FloatField(null=False)
    good_max_temp = models.FloatField(default=None)
    good_min_humid = models.FloatField(null=False)
    good_max_humid = models.FloatField(default=None)

class Other(models.Model):
    name = models.CharField(max_length=20, primary_key=True, null=False)
    good_min_temp = models.FloatField(null=False)
    good_max_temp = models.FloatField(default=None)
    good_min_humid = models.FloatField(null=False)
    good_max_humid = models.FloatField(default=None)

class Month_Season(models.Model):
    id = models.AutoField(primary_key=True,default=None)
    s_name = models.CharField(max_length=20, null=False)
    s_min_month = models.IntegerField() 
    s_max_month = models.IntegerField()
    s_season = models.CharField(default='', max_length=20, null=True)


