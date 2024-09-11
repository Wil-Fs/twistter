from django.shortcuts import render, redirect
from django.contrib.auth import authenticate


def login(request):
    logado = 'Voce precisa estar logado'
    return render(request, 'twistter/login.html', {'logado': logado})


def logout(request):
    pass