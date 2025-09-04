from rest_framework import generics, viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
