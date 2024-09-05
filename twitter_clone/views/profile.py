from django.shortcuts import render, redirect
from django.contrib import messages
from ..models import Profile


def profile(request, user):
    if request.user.is_authenticated:
        profiles = Profile.objects.filter(user_id=user)
        return render(request, 'twistter/profile.html', {
            'profiles': profiles
        })
    else:
        messages.warning(request, 'Você precisa está logado para acessar este conteúdo!')
        return redirect('home')