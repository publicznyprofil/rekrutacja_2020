import json

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from dashboard.models import AdvertisingData


yesterday = timezone.now().date() - timezone.timedelta(days=1)
today = timezone.now().date()


class DashboardViewTest(TestCase):
    url = reverse('dashboard:dashboard')

    def test_get(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertIn('data', response.context)
        self.assertIn('filters', response.context)

    def test_filter_by_data_source(self):
        AdvertisingData.objects.create(
            date=yesterday,
            clicks=5, impressions=3,
            data_source='GoogleAdsense',
            campaign='Campaign Name',
        )
        AdvertisingData.objects.create(
            date=today,
            clicks=5, impressions=3,
            data_source='GoogleAdsense',
            campaign='Other Campaign Name',
        )

        response = self.client.get(self.url, data={'campaign': 'Other Campaign Name'})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(json.loads(response.context['data'])), 1)
        self.assertEqual(json.loads(response.context['data'])[0]['date'], today.strftime('%Y-%m-%d'))

    def test_filter_by_campaign(self):
        AdvertisingData.objects.create(
            date=yesterday,
            clicks=5, impressions=3,
            data_source='GoogleAdsense',
            campaign='Campaign Name',
        )
        AdvertisingData.objects.create(
            date=today,
            clicks=5, impressions=3,
            data_source='Facebook',
            campaign='Other Campaign Name',
        )

        response = self.client.get(self.url, data={'data_source': 'GoogleAdsense'})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(json.loads(response.context['data'])), 1)
        self.assertEqual(json.loads(response.context['data'])[0]['date'], yesterday.strftime('%Y-%m-%d'))

    def test_filter_by_datasource_and_campaign(self):
        AdvertisingData.objects.create(
            date=yesterday,
            clicks=5, impressions=3,
            data_source='GoogleAdsense',
            campaign='Campaign Name',
        )
        AdvertisingData.objects.create(
            date=today,
            clicks=5, impressions=3,
            data_source='Facebook',
            campaign='Other Campaign Name',
        )

        response = self.client.get(self.url, data={'data_source': 'GoogleAdsense', 'campaign': 'Other Campaign Name'})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(json.loads(response.context['data'])), 0)


class DashboardJsonViewTest(TestCase):
    url = reverse('dashboard:dashboard_json')

    def test_get(self):
        AdvertisingData.objects.create(
            date=yesterday,
            clicks=5, impressions=3,
            data_source='GoogleAdsense',
            campaign='Campaign Name',
        )

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf-8'),
            [{"total_clicks": 5, "date": "2020-02-11", "total_impressions": 3}]
        )
