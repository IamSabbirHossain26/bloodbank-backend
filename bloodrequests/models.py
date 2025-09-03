from django.db import models
from django.contrib.auth.models import User

class BloodRequest(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="requests_made")
    blood_group = models.CharField(max_length=3)
    blood_type = models.CharField(max_length=1)
    date_required = models.DateField()
    hospital_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default="Pending")  # Pending, Accepted, Completed
    accepted_by = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL, related_name="requests_accepted"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.blood_group}{self.blood_type} needed at {self.hospital_name} ({self.status})"
