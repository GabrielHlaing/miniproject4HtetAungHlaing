from django import forms
from .models import Booking, Feedback


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['seats_booked']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ["rating", "comment"]
        widgets = {
            "rating": forms.HiddenInput(),
            "comment": forms.Textarea(attrs={"rows": 3}),
        }