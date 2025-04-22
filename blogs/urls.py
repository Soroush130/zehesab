from django.urls import path
from . import views

urlpatterns = [
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('create/', views.blog_create, name='blog_create'),
    path('update/<int:blog_id>/', views.blog_update, name='blog_update'),
]
