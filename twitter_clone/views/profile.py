from django.shortcuts import render, redirect
from django.contrib import messages
from ..models import Profile, Twist
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from ..forms import SignUpForm


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
        form = SignUpForm(request.POST or None, instance=current_user)
        if form.is_valid():
            form.save()
            login(request, current_user)
            messages.warning(request, f'@{request.user.username.lower()}, your profile has been updated!')
            return redirect('home')
        return render(request, 'twistter/update_user.html', {'form':form})
    else:
        messages.warning(request, 'You must be logged in to view that page!')
        return redirect('home')
