from django.db import models

class Timer(models.Model):
    "model for timer"
    aLength = models.IntegerField(null=True, blank=True)
    bLength = models.IntegerField(null=True, blank=True)