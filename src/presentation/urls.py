from django.urls import path
from django.contrib import admin
from .views import *


admin.autodiscover()


urlpatterns = [
    path('presentation/<int:user_id>/',
         presentation, name='presentation'),
    path('presentation/choose_present/',
         show_all_presentation, name='sprint_name'),
    path('presentation/sprint_name/<int:presentation_id>/',
         sprint_name, name='sprint_name'),
    path('presentation/completed/<int:presentation_id>/',
         completed, name='completed'),
    path('presentation/task_in_release/<int:presentation_id>/',
         task_in_release, name='task_in_release'),
    path('presentation/unfinished/<int:presentation_id>/',
         unfinished, name='unfinished'),
    path('presentation/total_story_points/<int:presentation_id>/',
         story_point, name='story_point'),
    path('presentation/planning_to_do/<int:presentation_id>/',
         planing_to_do, name='planing_to_do'),
    path('presentation/questions/<int:presentation_id>/',
         question, name='question'),
]