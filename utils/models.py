# Django Built-in modules
from django.db import models
from django.utils.translation import gettext_lazy as _


class AbstractDateTimeModel(models.Model):
    created = models.DateTimeField(
        _('created'),
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        _('updated'),
        auto_now=True,
    )

    class Meta:
        abstract = True
