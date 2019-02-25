from rest_framework import serializers
from . import models


class BookStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model   = models.BookStore
        fields  = (
            'id', 'title', 'author', 'isbn', 'publication'
        )

        def create (self, validated_data):
            book    = models.BookStore(
                title       = validated_data['title'],
                author      = validated_data['author'],
                isbn        = validated_data['isbn'],
                publication = validated_data['publication']

            )
            book.save()
            return book





class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for our user profile objects."""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Create and return a new user."""

        user = models.UserProfile(
            email=validated_data['email'],
            name=validated_data['name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
