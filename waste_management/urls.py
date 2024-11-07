from django.urls import path
from . import views

app_name = 'waste_management'

urlpatterns = [
    path('disposal_request/<int:bin_id>/', views.disposal_request, name='disposal_request'),
]

