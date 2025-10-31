from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('book/<int:event_id>/', views.book_event, name='book_event'),
]