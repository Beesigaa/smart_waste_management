from django.db import models

# Create your models here.
class WasteBin(models.Model):
    location = models.CharField(max_length=100)
    bin_type = models.CharField(max_length=50)
    capacity = models.FloatField()  # in liters
    current_level = models.FloatField(default=0)  # in liters
    last_emptied = models.DateTimeField(auto_now=True)

    def is_nearing_capacity(self):
        return self.current_level >= 0.8 * self.capacity  # Notify if 80% full
