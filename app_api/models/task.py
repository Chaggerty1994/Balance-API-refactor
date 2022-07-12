from operator import truediv
from django.db import models
from django.contrib.auth.models import User

from app_api.models.timer import Timer

class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='tasks')
    description = models.CharField(max_length=500)
    active = models.BooleanField
    timer = models.ForeignKey(
        Timer, on_delete=models.CASCADE, related_name='task_timer')
    team = models.BooleanField