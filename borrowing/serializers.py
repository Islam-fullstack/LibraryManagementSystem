from rest_framework import serializers
from .models import Borrowing


class BorrowingSerializer(serializers.ModelSerializer):
    # Read-only display fields
    book_title = serializers.CharField(source='book.title', read_only=True)
    member_name = serializers.SerializerMethodField()
    overdue = serializers.SerializerMethodField()

    # Write: accept FK ids
    book = serializers.PrimaryKeyRelatedField(
        queryset=__import__('books.models', fromlist=['Book']).Book.objects.all()
    )
    member = serializers.PrimaryKeyRelatedField(
        queryset=__import__('members.models', fromlist=['Member']).Member.objects.all()
    )

    class Meta:
        model = Borrowing
        fields = [
            'id', 'book', 'book_title', 'member', 'member_name',
            'borrow_date', 'due_date', 'return_date', 'overdue'
        ]

    def get_member_name(self, obj):
        return f"{obj.member.first_name} {obj.member.last_name}"

    def get_overdue(self, obj):
        return obj.is_overdue()