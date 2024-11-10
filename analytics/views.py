from django.shortcuts import render
from django.db import models  # Add this import
from waste_management.models import WasteBin

def dashboard(request):
    bins = WasteBin.objects.all()
    full_bins = bins.filter(current_level__gte=models.F('capacity')).count()
    return render(request, 'analytics/dashboard.html', {'full_bins': full_bins})

