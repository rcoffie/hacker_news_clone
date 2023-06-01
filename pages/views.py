from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from story.models import Story 
import datetime
# Create your views here.

def home(request):
    today = datetime.date.today()
    stories = Story.objects.all()[0:50]
    # stories = Story.objects.filter(created_at__gte=today)[0:50]
    return render(request, 'pages/homepage.html',{'stories':stories,})



def new(request):
    today = datetime.date.today()
    stories = Story.objects.filter(created_at__gte=today).order_by('-created_by')

    return render(request, 'pages/new.html',{'stories':stories})


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'pages/signup.html', {'form':form,})