from django.shortcuts import render, redirect
from django.contrib import messages
from ..models import Profile, Twist
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from ..forms import SignUpForm, ProfilePicForm


def profile(request, user):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=user)
        twists = Twist.objects.filter(user_id=user).order_by('-created_at')

        #Post form logic
        if request.method == "POST":
            #Get current user ID
            current_user_profile = request.user.profile
            #Get form data
            action = request.POST['follow']
            #Decide follow or unfollow
            if action == "unfollow":
                current_user_profile.follows.remove(profile)
            elif action == "follow":
                current_user_profile.follows.add(profile)
            current_user_profile.save()

        return render(request, 'twistter/profile.html', {
            'profile': profile,
            'twists': twists,
        })
    else:
        messages.warning(request, 'You must be logged in to view that page!')
        return redirect('home')

def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        current_profile = Profile.objects.get(user__id=request.user.id)
        user_form = SignUpForm(request.POST or None, request.FILES or None, instance=current_user)
        profile_user_form = ProfilePicForm(request.POST or None, request.FILES or None, instance=current_profile)

        if user_form.is_valid() and profile_user_form.is_valid():
            user_form.save()
            profile_user_form.save()
            login(request, current_user)
            messages.warning(request, f'@{request.user.username.lower()}, your profile has been updated!')
            return redirect('home')

        return render(request, 'twistter/update_user.html', {
            'user_form': user_form,
            'profile_user_form': profile_user_form
        })
    else:
        messages.warning(request, 'You must be logged in to view that page!')
        return redirect('home')


def followers(request, pk):
    if request.user.is_authenticated:
        if request.user.id == pk:
            profiles = Profile.objects.get(user_id=pk)

            return render(request, 'twistter/followers.html', {
                'profiles': profiles
            })
        else:
            return redirect('home')
    else:
        messages.warning(request, 'You must be logged in to view this page.')
        return redirect('login')


def follows(request, pk):
    if request.user.is_authenticated:
        if request.user.id == pk:
            profiles = Profile.objects.get(user_id=pk)

            return render(request, 'twistter/follows.html', {
                'profiles': profiles
            })
        else:
            return redirect('home')
    else:
        messages.warning(request, 'You must be logged in to view this page.')
        return redirect('login')