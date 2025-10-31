from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    available_seats = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.title} — {self.date}"
