from django.db import models

from app_api.models import team
from app_api.models.team import Team
from django.contrib.auth.models import User

class TeamMember(models.Model):
    team = models.ForeignKey(
        Team, on_delete=models.CASCADE)
    member = models.ForeignKey(User, on_delete=models.CASCADE)