from django.db import models

# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length=255)
    image = models.TextField(max_length=500)
    about = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title']
