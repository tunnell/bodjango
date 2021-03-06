from django.db import models
from django import forms
import datetime
# Create your models here.

class LogEntry(models.Model):
    message = models.CharField(max_length=5000)
    priority = models.IntegerField(default=5)
    time = models.DateTimeField(default=datetime.datetime.now, blank=True)
    
    class MongoMeta:
        db_table = "log"

class NewLog(forms.Form):
    message = forms.CharField(max_length=1000)