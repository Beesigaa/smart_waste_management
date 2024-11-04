from django.urls import path
from . import views

urlpatterns = [
    path('disposal_request/<int:bin_id>/', views.disposal_request, name='disposal_request'),
]

