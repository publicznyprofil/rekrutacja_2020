from django.db.models import QuerySet, Sum


class AdvertisingDataQuerySet(QuerySet):
    def transform_for_chart(self):
        return self.values('date').annotate(total_clicks=Sum('clicks'), total_impressions=Sum('impressions')).order_by()
