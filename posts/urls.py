from django.urls import path
from .views import home, list_load_posts_view

app_name = 'home'

urlpatterns = [
    path('', home, name='home'),
    path('posts/', list_load_posts_view, name='posts'),
]