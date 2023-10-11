from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostListAPIView.as_view(), name='post_list'),
    path('posts/<int:pk>/', views.PostDetailAPIView.as_view(), name='post_detail'),
    path('posts/<int:post_id>/bookmark/', views.BookmarkCreateAPIView.as_view(), name='bookmark_toggle'),
    path('bookmarks/', views.BookmarkListAPIView.as_view(), name='bookmark_list'),
    # path('authors/<int:pk>/', views.AuthorDetailAPIView.as_view(), name='author-detail'),
    # path('<slug:category_slug>/', views.CategoryPostListAPIView.as_view(), name='category_post_list'),
]
