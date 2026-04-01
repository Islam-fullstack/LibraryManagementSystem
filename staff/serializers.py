from rest_framework import serializers
from .models import Staff


class StaffSerializer(serializers.ModelSerializer):
    # Frontend expects 'name' and 'role' fields
    name = serializers.SerializerMethodField()
    role = serializers.CharField(source='position')

    class Meta:
        model = Staff
        fields = ['id', 'name', 'first_name', 'last_name', 'email', 'role', 'position', 'hire_date']

    def get_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"