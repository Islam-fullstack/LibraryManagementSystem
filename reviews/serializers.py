from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    book_title = serializers.CharField(source='book.title', read_only=True)
    member_name = serializers.SerializerMethodField()
    review_text = serializers.CharField(source='comment')  # ← maps frontend field to model field

    book = serializers.PrimaryKeyRelatedField(
        queryset=__import__('books.models', fromlist=['Book']).Book.objects.all()
    )
    member = serializers.PrimaryKeyRelatedField(
        queryset=__import__('members.models', fromlist=['Member']).Member.objects.all()
    )

    class Meta:
        model = Review
        fields = [
            'id', 'book', 'book_title', 'member', 'member_name',
            'rating', 'review_text', 'created_at'
        ]

    def get_member_name(self, obj):
        return f"{obj.member.first_name} {obj.member.last_name}"
