from rest_framework import serializers
from .models import Post, Category, Bookmark


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)


class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Post
        fields = '__all__'

    def get_cover_url(self, obj):
        request = self.context.get('request')
        if obj.cover:
            return request.build_absolute_uri(obj.cover.url)
        return None


class BookmarkSerializer(serializers.ModelSerializer):
    post = PostSerializer()

    class Meta:
        model = Bookmark
        fields = ('post',)
