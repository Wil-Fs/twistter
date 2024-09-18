from django.urls import path
from .views import (home, profile_list, profile, login_user, logout_user, register_user,
                    update_user, twist_like, twist_share, unfollow, follow, followers, follows,
                    delete_twist)

urlpatterns = [
    path("", home, name='home'),
    path('profile_list', profile_list, name='profile-list'),
    path('profile/<user>', profile, name='profile'),
    path('profile/followers/<int:pk>', followers, name='followers'),
    path('profile/follows/<int:pk>', follows, name='follows'),
    path('login', login_user, name='login'),
    path('logout', logout_user, name='logout'),
    path('register', register_user, name='register'),
    path('update_user', update_user, name='update-user'),
    path('twist_like/<pk>', twist_like, name='twist-like'),
    path('twist_share/<pk>', twist_share, name='twist-share'),
    path('unfollow/<pk>', unfollow, name='unfollow'),
    path('follow/<pk>', follow, name='follow'),
    path('delete_twist/<pk>', delete_twist, name='delete-twist'),
]
