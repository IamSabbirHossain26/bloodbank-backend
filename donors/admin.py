from django.contrib import admin
from .models import DonorProfile

@admin.register(DonorProfile)
class DonorProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'blood_group', 'blood_type', 'age', 'gender', 'is_available', 'last_donation_date')
    search_fields = ('user__username', 'blood_group', 'blood_type', 'address')
    list_filter = ('blood_group', 'blood_type', 'is_available')
