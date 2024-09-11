from django.shortcuts import render, redirect
from ..models import Twist

def home(request):
    if request.user.is_authenticated:
        twists = Twist.objects.all().order_by('-created_at')
        return render(request, 'twistter/home.html', {'twists': twists})
    else:
        return redirect('login')

def login(request):
    logado = 'Voce precisa estar logado'
    return render(request, 'twistter/login.html', {'logado': logado})