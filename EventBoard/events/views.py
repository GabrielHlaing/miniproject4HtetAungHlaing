from datetime import timedelta

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .forms import BookingForm, FeedbackForm
from .models import Event, Booking, Feedback


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

@login_required
def my_bookings(request):
    bookings = request.user.booking_set.select_related('event').order_by('-booking_date')
    return render(request, 'events/my_bookings.html', {'bookings': bookings})

@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if request.method == 'POST':
        event = booking.event
        event.save()
        booking.delete()
        messages.success(request, "Your booking has been canceled!")
        return redirect('events:my_bookings')

    return render(request, 'events/confirm_cancel.html', {'booking': booking})

def previous_events(request):
    today = timezone.now().date()
    filter_type = request.GET.get('filter', '7days')

    if filter_type == '7days':
        start_date = today - timedelta(days=7)
    elif filter_type == '1month':
        start_date = today - timedelta(days=30)
    elif filter_type == '3months':
        start_date = today - timedelta(days=90)
    else:
        start_date = None  # For > 3 months

    if start_date:
        events = Event.objects.filter(date__lt=today, date__gte=start_date)
    else:
        events = Event.objects.filter(date__lt=today - timedelta(days=90))

    context = {
        'events': events.order_by('-date'),
        'filter_type': filter_type,
    }
    return render(request, 'events/previous_events.html', context)

@login_required
def feedback(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            fb = form.save(commit=False)
            fb.user = request.user
            fb.save()
            return redirect("feedback")
    else:
        form = FeedbackForm()

    feedbacks = Feedback.objects.all().order_by("-created_at")
    return render(request, "events/feedback.html", {"form": form, "feedbacks": feedbacks})
