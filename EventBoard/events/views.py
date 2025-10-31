from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404

from .forms import BookingForm
from .models import Event, Booking


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

@login_required
def book_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            seats = form.cleaned_data['seats_booked']
            if seats <= 0:
                messages.error(request, "Invalid number of seats.")
            elif seats > event.available_seats:
                messages.error(request, "Not enough seats available.")
            else:
                Booking.objects.create(event=event, user=request.user, seats_booked=seats)
                messages.success(request, "Your booking was successful!")
                return redirect('events:index')
    else:
        form = BookingForm()

    return render(request, 'events/book_event.html', {'event': event, 'form': form})

