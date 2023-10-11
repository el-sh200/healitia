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
    name = serializers.CharField(source='user.name', required=False)

    class Meta:
        model = Profile
        exclude = ('user',)

    def create(self, validated_data):
        user = self.context['request'].user
        profile, created = Profile.objects.get_or_create(user=user, **validated_data)
        return profile

    def update(self, instance, validated_data):
        # Update the related user instance if necessary
        user_data = validated_data.pop('user', {})
        user = instance.user
        for attr, value in user_data.items():
            setattr(user, attr, value)
        user.save()

        # Update the profile instance
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance
