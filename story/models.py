from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Story(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name="stories", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title 
    

class Comment(models.Model):
    story = models.ForeignKey(Story, related_name="comments", on_delete=models.CASCADE)
    text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)