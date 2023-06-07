from django.shortcuts import render, redirect, get_object_or_404
from story.forms import StoryForm, CommentForm
from story.models import Story, Comment, Vote
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
    story.has_voted = False
    if request.user.is_authenticated:
         if story.votes.filter(created_by =request.user):
             story.has_voted = True
    comments = Comment.objects.filter(story=story)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.story = story
            comment.created_by = request.user 
            comment.save()
            return redirect('detail', id=id)
    else:
        form = CommentForm()
    return render(request, 'story/story_detail.html',{'story':story,'form':form,'comments':comments,})


def vote(request, id):
    story = Story.objects.get(id=id)
    already_voted = story.votes.filter(created_by=request.user )
    if not already_voted:
        Vote.objects.create(story=story, created_by=request.user)
    else:
        vote = Vote.objects.get(story_id=id, created_by=request.user)
        vote.delete()

    redirect_page = request.GET.get('redirect_page', '/')

    if redirect_page == "detail":
        return redirect("detail", id=id)
    else:
        return redirect(redirect_page)




