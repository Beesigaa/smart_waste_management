from django.db import models
from django.contrib.auth.models import User

class WasteBin(models.Model):
    location = models.CharField(max_length=100)
    capacity = models.IntegerField()  # max capacity of bin in liters
    current_level = models.IntegerField()  # current waste level in liters

    def is_full(self):
        return self.current_level >= self.capacity

class WasteDisposalRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bin = models.ForeignKey(WasteBin, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
