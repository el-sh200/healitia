from django.db import models
from django.utils.translation import gettext_lazy as _

from account.models import User
from utils.models import AbstractDateTimeModel


# Create your models here.
class Author(AbstractDateTimeModel):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name=_('user')
    )
    slug = models.SlugField(
        unique=True,
        max_length=100,
        verbose_name=_('slug')
    )
    display_name = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name=_('display name')
    )

    def __str__(self):
        return self.slug

    def get_display_name(self):
        return self.display_name if self.display_name else self.user.name


class Category(AbstractDateTimeModel):
    name = models.CharField(
        _('name'),
        max_length=50,
    )

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def __str__(self):
        return self.name


class Post(AbstractDateTimeModel):
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_('category')
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_('author')
    )
    title = models.CharField(
        _('title'),
        max_length=200,
    )
    text = models.TextField(
        verbose_name=_('text')
    )
    cover = models.ImageField(
        upload_to='post/cover/',
        null=True,
        blank=True,
        verbose_name=_('cover')
    )

    def __str__(self):
        return self.title


class Bookmark(AbstractDateTimeModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_('user')
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name=_('post'),
    )
    timestamp = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('timestamp')
    )

    class Meta:
        unique_together = ('user', 'post')

    def __str__(self):
        return f"{self.user.email}'s favorite - {self.post.title}"
