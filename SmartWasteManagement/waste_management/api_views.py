from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import WasteBin

@api_view(['GET'])
def bin_data(request):
    bins = WasteBin.objects.all()
    data = [{"location": bin.location, "level": bin.current_level} for bin in bins]
    return Response(data)

