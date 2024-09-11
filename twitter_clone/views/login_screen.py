from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.warning(request, f'You Have Been Logged In!, Welcome @{ request.user.username.lower() }')
            return redirect('home')
        else:
            messages.warning(request, f'There was an error loggin in. Try Again...')
            return redirect('login')
    else:
        return render(request, 'twistter/login.html', {})


def logout_user(request):
    logout(request)
    messages.warning(request, 'You Have Been Logged Out. See you soon!')
    return redirect('login')