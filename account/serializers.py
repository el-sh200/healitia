from rest_framework import serializers

# Local apps
from .models import User, Profile


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'name']


class ProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source='user.email', read_only=True)
    name = serializers.CharField(source='user.name', read_only=True)

    class Meta:
        model = Profile
        exclude = ('user',)

    def create(self, validated_data):
        user = self.context['request'].user
        profile, created = Profile.objects.get_or_create(user=user, **validated_data)
        return profile
