from django import forms
from django.forms import ModelForm

from story.models import Comment, Story


class StoryForm(ModelForm):
    class Meta:
        model = Story
        fields = ("title", "url", "text")
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Post Title"}
            ),
            "url": forms.TextInput(attrs={"class": "form-control"}),
            "text": forms.Textarea(attrs={"class": "form-control"}),
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ("text",)
        widgets = {"text": forms.Textarea(attrs={"class": "form-control"})}
