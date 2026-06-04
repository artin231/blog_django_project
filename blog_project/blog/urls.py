from django.urls import path 
from . import views


urlpatterns = [
    path('' , views.home,name='home'),
    path('posts/' , views.blog , name='blog'),
    path('posts/<name>',views.det_blog , name='det_blog'),
    path('about/',views.about , name='about')

]