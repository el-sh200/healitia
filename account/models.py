# Django Built-in modules
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

# Local apps
from .managers import UserManager
from utils.models import AbstractDateTimeModel


class User(AbstractBaseUser, PermissionsMixin, AbstractDateTimeModel):
    email = models.EmailField(
        _("email"),
        unique=True,
    )
    name = models.CharField(
        _('name'),
        max_length=200,
        null=True,
        blank=True,
    )
    is_superuser = models.BooleanField(
        _('superuser'),
        default=False,
    )
    is_staff = models.BooleanField(
        _('staff'),
        default=False,
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        ordering = ('-created',)
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.email
