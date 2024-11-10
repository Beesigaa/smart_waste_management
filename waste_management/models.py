from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class WasteBin(models.Model):
    location = models.CharField(max_length=100)
    capacity = models.IntegerField()  # max capacity of bin in liters
    current_level = models.IntegerField()  # current waste level in liters

    def is_full(self):
        return self.current_level >= self.capacity

    def __str__(self):
        return f"{self.location} (Capacity: {self.capacity}L)"

class WasteRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bin = models.ForeignKey(WasteBin, on_delete=models.CASCADE, related_name="requests")
    timestamp = models.DateTimeField(default=timezone.now)
    status = models.CharField(
        max_length=20,
        choices=[
            ('Pending', 'Pending'),
            ('In Progress', 'In Progress'),
            ('Completed', 'Completed'),
        ],
        default='Pending',
    )

    def __str__(self):
        return f"Disposal Request by {self.user.username} for {self.bin} - Status: {self.status}"

