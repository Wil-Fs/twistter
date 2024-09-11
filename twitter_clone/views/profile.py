from django.shortcuts import render, redirect
from django.contrib import messages
from ..models import Profile, Twist


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
        messages.warning(request, 'Você precisa está logado para acessar este conteúdo!')
        return redirect('home')