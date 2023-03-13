from django.db import models

# Create your models here.

class Teams(models.Model):
    team_name = models.CharField(max_length = 25)
    nick_name = models.CharField(max_length = 5)