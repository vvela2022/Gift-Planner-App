from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length=255)
    image = models.TextField(max_length=500)
    about = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title']


class Gift_Idea(models.Model):
    idea = models.CharField(max_length=255)
    image = models.TextField(max_length=500)
    link = models.TextField(max_length=255)
    date_needed = models.DateField()
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='gifts')

    def __str__(self):
        return self.idea
