from django.db import models

from dashboard.managers import AdvertisingDataQuerySet


class AdvertisingData(models.Model):
    date = models.DateField()
    data_source = models.CharField(max_length=255)
    campaign = models.CharField(max_length=255)
    clicks = models.PositiveIntegerField()
    impressions = models.PositiveIntegerField()
    created_date = models.DateTimeField(auto_now_add=True)

    objects = AdvertisingDataQuerySet.as_manager()
