from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import DonorProfile
from .serializers import DonorProfileSerializer
from users.permissions import IsOwnerOrReadOnly  # ✅ Import custom permission

class DonorProfileViewSet(viewsets.ModelViewSet):
    queryset = DonorProfile.objects.all()
    serializer_class = DonorProfileSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
