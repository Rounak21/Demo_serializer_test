from django.db import models
from datetime import datetime
# Create your models here.

class Comment(models.Model):
    
    author_name=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    detail=models.TextField()
    created=models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.title
