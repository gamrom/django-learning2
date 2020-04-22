from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    class Meta:
        ordering = ['-create_at']

    title = models.CharField(max_length= 200)
    content = models.TextField()
    view_content = models.IntegerField(default= 0)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
