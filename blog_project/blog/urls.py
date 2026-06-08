from django.urls import path 
from . import views


urlpatterns = [
    path('' , views.home,name='home'),
    path('posts/' , views.blogg , name='blog'),
    path('posts/<slug:name>',views.det_blog , name='det_blog'),
    path('about/',views.about , name='about'),
    path('make_blog/',views.make_blog , name='make'),
    path('posts/' , views.blog , name='blog'),
    path('posts/<name>',views.det_blog , name='det_blog'),
    path('about/',views.about , name='about')

]