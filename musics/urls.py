from . import views
from django.urls import path

urlpatterns = [
    path('musics/',views.music_list ),
    ]