from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),

    path('logout/', views.log_out, name='logout'),
    path('profile/', views.profile, name='profile'),
]
