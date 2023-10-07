from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.models import AbstractDateTimeModel


class Subscriber(AbstractDateTimeModel):
    email = models.EmailField(
        _("email"),
        unique=True,
        max_length=200,
    )
    date_subscribed = models.DateTimeField(
        _('date_subscribed'),
        auto_now_add=True,
    )

    class Meta:
        verbose_name = _('subscriber')
        verbose_name_plural = _('subscribers')

    def __str__(self):
        return self.email
