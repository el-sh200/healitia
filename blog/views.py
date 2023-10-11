from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView

from .models import Post, Category, Bookmark
from .serializers import PostSerializer, CategorySerializer, BookmarkSerializer


class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# class CategoryPostListAPIView(generics.ListAPIView):
#     serializer_class = PostSerializer
#
#     def get_queryset(self):
#         category_slug = self.kwargs['category_slug']
#         return Post.objects.filter(category__slug=category_slug)


class PostDetailAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class BookmarkCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        user = request.user
        Bookmark.objects.get_or_create(post=post, user=user)

        return JsonResponse({'message': 'created'}, status=status.HTTP_200_OK)

    def delete(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        user = request.user
        bookmark, created = Bookmark.objects.get_or_create(post=post, user=user)
        bookmark.delete()

        return JsonResponse({'message': 'deleted'}, status=status.HTTP_200_OK)


class BookmarkListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BookmarkSerializer

    def get_queryset(self):
        user = self.request.user

        return Bookmark.objects.filter(user=user)

# class AuthorDetailAPIView(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = AuthorSerializer
