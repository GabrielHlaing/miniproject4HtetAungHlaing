from django.contrib.auth.models import User
from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    total_seats = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.title} — {self.date}"

    @property
    def available_seats(self):
        booked = sum(booking.seats_booked for booking in self.bookings.all())
        return self.total_seats - booked

class Booking(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='bookings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seats_booked = models.PositiveIntegerField()
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} booked {self.seats_booked} seat(s) for {self.event.name}"