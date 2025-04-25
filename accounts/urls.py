from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),

    path('logout/', views.log_out, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile_image, name='edit_profile_image'),
    path('profile/remove_profile_image/', views.remove_profile_image, name='remove_profile_image'),
]
