from django.urls import path 
from . import views


urlpatterns = [
    path('' , views.home,name='home'),
    path('posts/' , views.blog , name='blog'),
    # path('posts/<slug:slug>')

]