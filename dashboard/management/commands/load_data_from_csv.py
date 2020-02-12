import time

from django.core.management.base import BaseCommand

from dashboard.data_loader import load_data_from_csv


class Command(BaseCommand):
    help = 'Load data from csv into model'

    def handle(self, *args, **options):
        start_time = time.perf_counter()

        load_data_from_csv()

        self.stdout.write(
            self.style.SUCCESS(
                'Successfully loaded data, it took {}'.format(time.perf_counter() - start_time)
            )
        )
