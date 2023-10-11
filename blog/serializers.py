from rest_framework import serializers
from .models import Post, Category, Bookmark


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)


class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    is_bookmarked = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'

    def get_cover_url(self, obj):
        request = self.context.get('request')
        if obj.cover:
            return request.build_absolute_uri(obj.cover.url)
        return None

    def get_is_bookmarked(self, instance):
        user = self.context['request'].user
        if user.is_authenticated:
            return Bookmark.objects.filter(user=user, post=instance).exists()
        return False


class BookmarkSerializer(serializers.ModelSerializer):
    post = PostSerializer()
    class Meta:
        model = Bookmark
        fields = ('post',)
