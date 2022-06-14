from django.db import models
from django.contrib.auth.models import User


class ChatPost(models.Model):
  user  = models.ForeignKey(User, on_delete=models.CASCADE)
  content = models.CharField(max_length=500)
  date_added = models.DateTimeField(auto_now_add=True)
  
  class Meta:
    ordering = ['-date_added']
  