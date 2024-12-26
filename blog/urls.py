from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.CreateBlogView.as_view(), name='create-blog'),
    path('<int:pk>/', views.RetrieveBlogView.as_view(), name='retrieve-blog'),
    path('create/', views.CreatePostView.as_view(), name='create-post')
]

