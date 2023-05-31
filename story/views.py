from django.shortcuts import render, redirect, get_object_or_404
from story.forms import StoryForm 
from story.models import Story
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
    return render(request, 'story/story_detail.html',{'story':story})