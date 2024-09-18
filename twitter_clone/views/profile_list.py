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
        messages.warning(request, 'You must be logged in to view this page.')
        return redirect('login')


def unfollow(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        request.user.profile.follows.remove(profile)
        request.user.profile.save()

        messages.warning(request, f'You unfollowed @{profile.user.username.lower()}')
        return redirect(request.META.get("HTTP_REFERER"))
    else:
        messages.warning(request, 'You must be logged in to view this page.')
        return redirect('login')


def follow(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        request.user.profile.follows.add(profile)
        request.user.profile.save()

        messages.warning(request, f'You followed @{profile.user.username.lower()}')
        return redirect(request.META.get("HTTP_REFERER"))
    else:
        messages.warning(request, 'You must be logged in to view this page.')
        return redirect('login')