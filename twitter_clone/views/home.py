from django.shortcuts import render

def home(request):
    text = 'Hi, good luck!'
    return render(request, 'twistter/home.html', {'text': text})