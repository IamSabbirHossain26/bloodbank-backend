from rest_framework import viewsets
from .models import DonorProfile
from .serializers import DonorProfileSerializer

class DonorProfileViewSet(viewsets.ModelViewSet):
    queryset = DonorProfile.objects.all()
    serializer_class = DonorProfileSerializer

