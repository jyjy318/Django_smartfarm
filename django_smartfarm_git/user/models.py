from django.db import models

class User(models.Model):
    user_id = models.CharField(max_length=20, primary_key=True, null=False)
    name = models.CharField(max_length=20)
    pw = models.CharField(max_length=64)

