from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
# Create your views here.

def home(request):

    return render(request, 'pages/homepage.html')


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'pages/signup.html', {'form':form,})