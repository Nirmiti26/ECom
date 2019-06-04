from django.db import models


class Solar(models.Model):
    pincode = models.IntegerField()
    load = models.IntegerField(default=1)
    roofArea = models.FloatField(default=120)
