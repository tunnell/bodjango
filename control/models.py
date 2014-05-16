from django.db import models
from django import forms

# Create your models here.

class rateInfo(models.Model):
    node = models.CharField(max_length=100)
    bltrate = models.DecimalField(max_digits=5, decimal_places=2)
    datarate = models.DecimalField(max_digits=5,decimal_places=2)
    runmode = models.CharField(max_length=100)
    createdAt = models.DateTimeField(null=True, blank=True)
    timeseconds = models.IntegerField(default=0)
    nboards = models.IntegerField(default=0)
    class MongoMeta:
        db_table = "rates"

class DAQStatus(models.Model):
    createdAt = models.DateTimeField(null=True, blank=True)
    expireAfterSeconds = models.IntegerField(default=0)
    timeseconds = models.IntegerField(default=0)
    mode = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    network = models.BooleanField()
    currentRun = models.CharField(max_length=100)
    startedBy = models.CharField(max_length=100)
    numSlaves = models.IntegerField(default=0)
    class MongoMeta:
        db_table = "daqstatus"

class DAQCommand(forms.Form):
    command = forms.CharField(max_length=100)
    mode = forms.CharField(max_length=100)
    name = forms.CharField(max_length=100)

class DAQCommandDBEntry(models.Model):
    command = models.CharField(max_length=100)
    mode = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    class MongoMeta:
        db_table = "daqcommands"
    