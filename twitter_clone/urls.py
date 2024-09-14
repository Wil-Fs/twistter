from django.urls import path
from .views import home, profile_list, profile, login_user, logout_user, register_user, update_user

urlpatterns = [
    path("", home, name='home'),
    path('profile_list', profile_list, name='profile-list'),
    path('profile/<user>', profile, name='profile'),
    path('login', login_user, name='login'),
    path('logout', logout_user, name='logout'),
    path('register', register_user, name='register'),
    path('update_user', update_user, name='update-user'),
]
