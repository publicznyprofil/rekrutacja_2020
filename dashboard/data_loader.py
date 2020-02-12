import csv
import datetime
import os

from django.conf import settings

from dashboard.models import AdvertisingData


def load_data_from_csv():
    AdvertisingData.objects.bulk_create(
        get_advertising_data_object_list()
    )


def get_advertising_data_object_list():
    file_path = os.path.join(settings.BASE_DIR, 'dashboard', 'data.csv')
    objects = []

    with open(file_path) as _file:
        reader = csv.DictReader(_file)
        for row in reader:
            objects.append(
                AdvertisingData(
                    date=datetime.datetime.strptime(row['Date'], '%d.%m.%Y'),
                    data_source=row['Datasource'],
                    campaign=row['Campaign'],
                    clicks=int(row['Clicks']),
                    impressions=int(row['Impressions']) if row['Impressions'] else 0,
                )
            )

    return objects
