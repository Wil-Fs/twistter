from django.urls import path
from .views import home, profile_list, profile

urlpatterns = [
    path("", home, name='home'),
    path('profile_list', profile_list, name='profile-list'),
    path('profile/<user>', profile, name='profile')
]
