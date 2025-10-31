from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .models import Event

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("events:index")   # go to home after sign up
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})

def index(request):
    events = Event.objects.all().order_by('date')
    return render(request, 'events/index.html', {'events': events})
