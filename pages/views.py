from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from story.models import Story 
from pages.models import Profile, Follow
import datetime
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    today = datetime.date.today()
    stories = Story.objects.all()[0:50]
    # stories = Story.objects.filter(created_at__gte=today)[0:50]
    return render(request, 'pages/homepage.html',{'stories':stories,})


@login_required
def new(request):
    today = datetime.date.today()
    user = request.user.profile
    print(user)

    following = user.follower.all()
    print(following.count)
    stories = Story.objects.all()
    return render(request, 'pages/new.html',{'stories':stories})


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            new_user = form.save()
            Profile.objects.create(user=new_user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'pages/signup.html', {'form':form,})

@login_required
def profile(request):
    profile = request.user.profile
    stories = Story.objects.filter(created_by=request.user)
    print(request.user)
    return render(request,'pages/profile.html', {'profile':profile,'stories':stories})

def user_profile(request, id):
    user_profile = Profile.objects.get(id=id)
    user_profile.is_following = False
    if request.user.is_authenticated:
        if user_profile.following.filter(follower=request.user.profile):
            user_profile.is_following = True
    
    user = user_profile.user
    stories = Story.objects.filter(created_by=user)
    return render(request, 'pages/user_profile.html',{'user_profile':user_profile,'stories':stories})


def follow(request, id):
    author = Profile.objects.get(id=id)
    user = request.user.profile
    is_following = author.following.filter(follower=request.user.profile)
    if not is_following:
        Follow.objects.create(follower=user, following=author)
    else:
        follow = Follow.objects.get(following_id=author.id, follower=user)
        follow.delete()
    return redirect('user_profile', id=id)


