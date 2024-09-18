from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from ..models import Twist, Profile
from ..forms import TwistForm
from django.contrib.auth.models import User

def home(request):
    if request.user.is_authenticated:
        form = TwistForm(request.POST or None)

        if request.method == "POST":
            if form.is_valid():
                twist = form.save(commit=False)
                twist.user = request.user
                twist.save()
                messages.warning(request, 'Your Twist Has Been Posted!')
                return redirect('home')

        twists = Twist.objects.filter(user__profile__followed_by=request.user.profile).order_by('-created_at')

        return render(request, 'twistter/home.html', {
            'twists': twists,
            'form': form
        })
    else:
        return redirect('login')

def twist_like(request, pk):
    if request.user.is_authenticated:
        twist = get_object_or_404(Twist, id=pk)
        if twist.likes.filter(id=request.user.id):
            twist.likes.remove(request.user)
        else:
           twist.likes.add(request.user)
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('login')


def twist_share(request, pk):
    if request.user.is_authenticated:
        twist = get_object_or_404(Twist, id=pk)
        if twist:
            messages.warning(request, 'Twist!')
        else:
            return redirect('home')
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('login')

def delete_twist(request, pk):
    if request.user.is_authenticated:
        twist = get_object_or_404(Twist, id=pk)
        if request.user.username == twist.user.username:
            twist.delete()
            messages.warning(request, 'Your Twist has been deleted!')
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            redirect('home')
    else:
        return redirect('login')

def edit_twist(request, pk):
    if request.user.is_authenticated:
        twist = get_object_or_404(Twist, id=pk)
        if request.user.username == twist.user.username:
            form = TwistForm(request.POST or None, instance=twist)
            if request.method == "POST":
                if form.is_valid():
                    twist = form.save(commit=False)
                    twist.user = request.user
                    twist.save()
                    messages.warning(request, 'Your Twist has been updated!')
                    return redirect('home')
            else:
                return render(request, 'twistter/edit_twist.html', {
                    'twist': twist,
                    'form': form,
                })
        else:
            return redirect('login')

    else:
        return redirect('login')

def search_twistt(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            search = request.POST['search']
            searched = Twist.objects.filter(body__contains=search)
            return render(request, 'twistter/search_twistt.html', {
                'search': search,
                'searched':searched
            })
        else:
            return render(request, 'twistter/search_twistt.html', {})
    else:
        return redirect('login')

def search_user(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            search = request.POST['search']
            searched = User.objects.filter(username__contains=search)
            return render(request, 'twistter/search_user.html', {
                'search': search,
                'searched':searched
            })
        else:
            return render(request, 'twistter/search_user.html', {})
    else:
        return redirect('login')