from unittest.mock import patch, mock_open

from django.test import TestCase

from dashboard.data_loader import load_data_from_csv
from dashboard.models import AdvertisingData


class LoadDataFromCSVTest(TestCase):
    @patch('builtins.open', new_callable=mock_open)
    def test_load_data_from_csv(self, open_mocked):
        # mock_open doesn't properly handle iterating over the open file with for line in file:
        # but if we set the return value like this, it works.
        # it was fixed in python 3.7 https://bugs.python.org/issue32933
        data = [
            'Date,Datasource,Campaign,Clicks,Impressions',
            '01.01.2019,Facebook Ads,Like Ads,274,1979'
        ]
        open_mocked.return_value.__iter__.return_value = data

        load_data_from_csv()

        self.assertEqual(AdvertisingData.objects.all().count(), 1)

    @patch('dashboard.data_loader.open', new_callable=mock_open)
    def test_load_data_from_csv_without_impression_is_valid(self, open_mocked):
        # mock_open doesn't properly handle iterating over the open file with for line in file:
        # but if we set the return value like this, it works.
        # it was fixed in python 3.7 https://bugs.python.org/issue32933
        data = [
            'Date,Datasource,Campaign,Clicks,Impressions',
            '01.01.2019,Facebook Ads,Like Ads,274,'
        ]
        open_mocked.return_value.__iter__.return_value = data

        load_data_from_csv()

        self.assertEqual(AdvertisingData.objects.all().count(), 1)
