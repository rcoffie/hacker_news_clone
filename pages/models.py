from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=100, blank=True, null=True)
    profile_picture = models.ImageField(
        upload_to="profile_picture", null=True, blank=True
    )
    about = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Follow(models.Model):
    following = models.ForeignKey(
        Profile, related_name="following", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    follower = models.ForeignKey(
        Profile, related_name="follower", on_delete=models.CASCADE
    )
