from django.contrib import admin
from .models import Event, Booking, Feedback


# --- Event Admin ---
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location', 'total_seats', 'available_seats')
    search_fields = ('title', 'location')
    list_filter = ('date', 'location')
    ordering = ('-date',)


# --- Booking Admin ---
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('event', 'user', 'seats_booked', 'booking_date')
    search_fields = ('event__title', 'user__username')
    list_filter = ('booking_date', 'event')
    ordering = ('-booking_date',)


# --- Feedback Admin ---
@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating', 'comment', 'created_at')
    search_fields = ('user__username', 'comment')
    list_filter = ('rating', 'created_at')
    ordering = ('-created_at',)
