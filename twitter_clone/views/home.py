from django.shortcuts import render, redirect
from django.contrib import messages
from ..models import Twist
from ..forms import TwistForm

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

        twists = Twist.objects.all().order_by('-created_at')
        return render(request, 'twistter/home.html', {
            'twists': twists,
            'form': form
        })
    else:
        return redirect('login')
