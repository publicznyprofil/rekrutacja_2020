from django.test import TestCase
from django.utils import timezone

from dashboard.models import AdvertisingData


class AdvertisingDataQuerySetTest(TestCase):
    def test_transform_for_chart(self):
        yesterday = timezone.now().date() - timezone.timedelta(days=1)
        today = timezone.now().date()

        AdvertisingData.objects.create(
            date=yesterday,
            clicks=5, impressions=3
        )
        AdvertisingData.objects.create(
            date=today,
            clicks=10, impressions=2
        )
        AdvertisingData.objects.create(
            date=today,
            clicks=5, impressions=2
        )

        self.assertEqual(
            list(AdvertisingData.objects.transform_for_chart()),
            [
                {'date': yesterday, 'total_clicks': 5, 'total_impressions': 3},
                {'date': today, 'total_clicks': 15, 'total_impressions': 4},
            ]
        )
