from django.contrib import admin
from .models import Author, Category, Post, Bookmark

# Register your models here.
admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Bookmark)
