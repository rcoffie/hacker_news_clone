from django.shortcuts import render, redirect, get_object_or_404
from story.forms import StoryForm, CommentForm
from story.models import Story, Comment
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def create_story(request):
    form = StoryForm() 
    if request.method == "POST":
        form = StoryForm(request.POST)
        if form.is_valid():
            story = form.save(commit=False)
            story.created_by = request.user 
            story.save()
            return redirect('home')
    else:
        form = StoryForm()

    return render(request, 'story/create_story.html', {'form':form})


def story_detail(request, id):
    story = Story.objects.get(id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.story = story
            comment.created_by = request.user 
            comment.save()
    return render(request, 'story/story_detail.html',{'story':story})


def create_comment(request):

    return render(request, 'story/create_comment.html', {})