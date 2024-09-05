from django.shortcuts import render, redirect
from django.contrib import messages
from ..models import Profile
def profile_list(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user=request.user.id)
        return render(request, 'twistter/profile_list.html', {
            'profiles': profiles
        })
    else:
        messages.warning(request, 'Você precisa está logado para acessar este conteúdo!')
        return redirect('home')