from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    full_name = models.CharField(max_length=150, blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    blood_group = models.CharField(max_length=5, blank=True, null=True)  # A+, B-, etc.
    address = models.TextField(blank=True, null=True)
    last_donation_date = models.DateField(blank=True, null=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.user.email if self.user.email else self.user.username
