from django.urls import path
from django.contrib import admin
from .views import *


admin.autodiscover()


urlpatterns = [
    path('', home_page, name='home_page'),
    path('login/', authorization, name='login'),
    path('logout/', log_out, name='logout'),
    path('show_config/<int:user_id>/', show_config, name='show_config'),
    path('edit/<int:user_id>/', edit, name='edit'),
    path('delete/<int:user_id>/', delete, name='delete'),
    path('registration/', registration, name='registration'),
    path('account/', account_page, name='account_page'),
    path('create_config/', create_config, name='create_config'),
    path('pick_config/', choose_config_for_presentation, name='pick_config'),
]