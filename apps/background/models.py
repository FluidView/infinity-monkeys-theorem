from uuid import uuid4
from django.db import models

# Create your models here.

class statistic(models.Model):
    errors = models.IntegerField()
    bestStreakSize = models.IntegerField()
    bestStreak = models.CharField(max_length=175151, null=True, blank=True)
    
    

class best(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    word = models.CharField(max_length=175151)
    created_at = models.DateTimeField(auto_now_add=True)
    
class basic(models.Model):
    hamlet = models.CharField(max_length=175151)
    created_at = models.DateTimeField(auto_now_add=True)
    