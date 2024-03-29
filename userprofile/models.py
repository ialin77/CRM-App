from django.db import models
from django.contrib.auth.models import User
from team.models import Team

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    active_team = models.ForeignKey(Team, related_name='userprofile', blank=True, null=True, on_delete=models.CASCADE)

    def get_active_team(self):
        if self.active_team:
            return self.active_team
        else:
            return Team.objects.filter(members__in=[self.user.id]).first()

    def __str__(self):
        return str(self.user)