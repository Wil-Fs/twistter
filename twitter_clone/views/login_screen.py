from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from ..forms import SignUpForm

def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.warning(request, f'You Have Been Logged In!, Welcome @{request.user.username.lower()}')
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

def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']

            #Log in User
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.warning(request, f'You have successfuly registered! Welcome @{user.username.lower()}')
            return redirect('home')
    return render(request, 'twistter/register.html', {'form': form})