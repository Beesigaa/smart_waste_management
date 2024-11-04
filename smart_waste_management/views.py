# smart_waste_management/views.py
from django.shortcuts import render

def landing_page(request):
    return render(request, 'home.html')

