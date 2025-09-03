from rest_framework import viewsets
from .models import BloodRequest
from .serializers import BloodRequestSerializer

class BloodRequestViewSet(viewsets.ModelViewSet):
    queryset = BloodRequest.objects.all()
    serializer_class = BloodRequestSerializer
