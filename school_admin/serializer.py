from rest_framework import serializers
from .models import Admin

class AdminSerializers(serializers.ModelSerializer):
    class Meta:
        model=Admin
        fields='__all__'