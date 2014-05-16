from django.db import models
from django import forms

# Create your models here.

class TriggerrateInfo(models.Model):
    ratetoss = models.DecimalField(max_digits=5,decimal_places=2)
    rateout = models.DecimalField(max_digits=5,decimal_places=2)
    createdAt = models.DateTimeField(null=True, blank=True)
    time = models.IntegerField(default=0)

    class MongoMeta:
        db_table = "triggerrate"
