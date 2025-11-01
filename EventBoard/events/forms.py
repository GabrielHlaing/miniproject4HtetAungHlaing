from django import forms
from .models import Booking, Feedback


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['seats_booked']
        widgets = {
            'seats_booked': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1,
                'placeholder': 'Enter number of seats'
            })
        }
        labels = {
            'seats_booked': 'Number of Seats'
        }

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ["rating", "comment"]
        widgets = {
            "rating": forms.HiddenInput(),
            "comment": forms.Textarea(attrs={
                "rows": 3,
                "class": "form-control",
                "placeholder": "Write your feedback here..."
            }),
        }
