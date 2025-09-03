from django.contrib import admin
from .models import BloodRequest

@admin.register(BloodRequest)
class BloodRequestAdmin(admin.ModelAdmin):
    list_display = ('blood_group', 'blood_type', 'hospital_name', 'location', 'status', 'created_by', 'accepted_by', 'created_at')
    search_fields = ('hospital_name', 'location', 'contact_info')
    list_filter = ('blood_group', 'blood_type', 'status')
