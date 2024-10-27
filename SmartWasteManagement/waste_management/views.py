from django.shortcuts import render
from .models import WasteBin, CollectionRoute

# Create your views here.
def dashboard(request):
    bins = WasteBin.objects.all()
    routes = CollectionRoute.objects.all()
    context = {
        'bins': bins,
        'routes': routes,
        # Additional metrics and trends can be added here
    }
    return render(request, 'dashboard.html', context)
