from rest_framework import serializers
from .models import License


class LicenseSerializer(serializers.ModelSerializer):
    class Meta():
        model = License
        fields = ['id', 'company_name', 'user_full_name', 'job_title', 'user_email', 'software_user_name', 'expiration_date', 'version']