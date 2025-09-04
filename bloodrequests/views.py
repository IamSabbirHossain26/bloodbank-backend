from rest_framework import viewsets, status, serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import BloodRequest
from .serializers import BloodRequestSerializer

class AcceptRequestSerializer(serializers.Serializer):
    confirm = serializers.BooleanField(default=True)

class BloodRequestViewSet(viewsets.ModelViewSet):
    queryset = BloodRequest.objects.all().order_by('-created_at')
    serializer_class = BloodRequestSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    @action(
        detail=True,
        methods=['post'],
        permission_classes=[IsAuthenticated],   # ✅ শুধুমাত্র logged-in user accept করতে পারবে
        serializer_class=AcceptRequestSerializer
    )
    def accept(self, request, pk=None):
        blood_request = self.get_object()
        if blood_request.status == "Pending":
            blood_request.status = "Accepted"
            blood_request.accepted_by = request.user
            blood_request.save()
            return Response({"status": "Request accepted!"})
        return Response(
            {"error": "Request already accepted or completed."},
            status=status.HTTP_400_BAD_REQUEST
        )
