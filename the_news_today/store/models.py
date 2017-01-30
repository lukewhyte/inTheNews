from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

class Headlines(models.Model):
    BBC = models.CharField(max_length=200)
    CNN = models.CharField(max_length=200)
    aljazeera = models.CharField(max_length=200)
    fox = models.CharField(max_length=200)
    date = models.DateField(default=timezone.now)
