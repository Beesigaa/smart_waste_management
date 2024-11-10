from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import WasteBin, WasteRequest

# Create your views here.
@login_required
def disposal_request(request, bin_id):
    bin = WasteBin.objects.get(id=bin_id)
    if bin.is_full():
        # Alert that the bin is full
        return render(request, 'waste_management/bin_full.html', {'bin': bin})
    else:
        WasteRequest.objects.create(user=request.user, bin=bin)
        return redirect('dashboard')
