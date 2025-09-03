from django.db import models
from django.contrib.auth.models import User

class DonorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="donor_profile")
    blood_group = models.CharField(max_length=3)   # A, B, AB, O
    blood_type = models.CharField(max_length=1)    # + or -
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    address = models.TextField()
    last_donation_date = models.DateField(null=True, blank=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} - {self.blood_group}{self.blood_type}"
