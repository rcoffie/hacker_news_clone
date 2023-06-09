from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from pages import views

urlpatterns = [
    path("", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path("login/", LoginView.as_view(template_name="pages/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/", views.profile, name="profile"),
    path("user_profile/<int:id>/", views.user_profile, name="user_profile"),
    path("<int:id>/follow/", views.follow, name="follow"),
]
