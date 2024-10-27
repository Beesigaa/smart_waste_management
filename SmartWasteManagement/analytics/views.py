from django.shortcuts import render
from .models import CollectionRecord

# Create your views here.
def generate_report(request):
    records = CollectionRecord.objects.all()
    context = {
        'records': records,
        # Generate more insights and summary statistics here
    }
    return render(request, 'report.html', context)
