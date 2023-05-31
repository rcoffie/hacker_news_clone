from django.contrib import admin
from story.models import Story, Comment
# Register your models here.
admin.site.register(Story)
admin.site.register(Comment)