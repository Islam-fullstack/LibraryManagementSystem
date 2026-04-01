from rest_framework import serializers
from .models import Member, Role


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name', 'description']
        # ← removed 'members' reverse relation (circular)


class MemberSerializer(serializers.ModelSerializer):
    # Computed full name for frontend display
    name = serializers.SerializerMethodField()
    role_detail = RoleSerializer(source='role', read_only=True)
    role = serializers.PrimaryKeyRelatedField(
        queryset=Role.objects.all(), allow_null=True, required=False
    )
    phone = serializers.CharField(source='phone_number', required=False, allow_blank=True)

    class Meta:
        model = Member
        fields = [
            'id', 'name', 'first_name', 'last_name', 'email',
            'phone', 'phone_number', 'membership_date', 'role', 'role_detail'
        ]

    def get_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

    def create(self, validated_data):
        # Handle 'name' split if frontend sends it
        return super().create(validated_data)