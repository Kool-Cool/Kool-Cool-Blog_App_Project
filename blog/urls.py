from django.contrib import admin
from django.urls import path

from .views import BlogListView 
from .views import BlogDetailView 
from .views import BlogCreateView #new
from .views import BlogUpdateView # newnew
from .views import BlogDeleteView #newnewnwe
urlpatterns = [

    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'), #newnewnew
    path("post/<int:pk>/edit/",BlogUpdateView.as_view() , name = "post_edit"),
    path('post/new',BlogCreateView.as_view() , name='post_new') , #new
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'), 
    path("",BlogListView.as_view() , name='home')

]