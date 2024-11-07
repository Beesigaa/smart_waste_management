from django.db import models
from django.shortcuts import render
from waste_management.models import WasteBin, WasteDisposalRequest
# Create your views here.
def dashboard(request):
    bins = WasteBin.objects.all()
    total_bins = bins.count()
    full_bins = bins.filter(current_level__gte=models.F('capacity')).count()
    total_requests = WasteDisposalRequest.objects.count()
    return render(request, 'analytics/dashboard.html', {
        'total_bins': total_bins,
        'full_bins': full_bins,
        'total_requests': total_requests,
    })
