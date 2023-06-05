from django.urls import path
from story import views

urlpatterns = [
   path('create_story/', views.create_story, name="create_story"),
   path('<int:id>/', views.story_detail, name='detail'),
   path('<int:id>/vote/',views.vote, name='vote'),
]
