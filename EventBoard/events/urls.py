from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('detail/<int:event_id>/', views.event_detail, name='event_detail'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('cancel-booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('previous_events/', views.previous_events, name='previous_events'),
    path('feedback/', views.feedback, name='feedback'),
]