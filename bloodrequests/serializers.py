from rest_framework import serializers
from .models import BloodRequest

class BloodRequestSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    accepted_by = serializers.ReadOnlyField(source='accepted_by.username')

    class Meta:
        model = BloodRequest
        fields = "__all__"
