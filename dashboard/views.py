import json

from django.core.serializers.json import DjangoJSONEncoder
from django.views.generic import TemplateView

from dashboard.models import AdvertisingData


class DashboardView(TemplateView):
    template_name = 'dashboard/dashboard.html'
    filters_name = ['data_source', 'campaign']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = self.get_data()
        context['filters'] = self.get_filters()
        return context

    def get_data(self):
        queryset = self.get_filtered_queryset()
        return json.dumps(list(queryset.transform_for_chart()), cls=DjangoJSONEncoder)

    def get_filters(self):
        return {
            'data_source': list(AdvertisingData.objects.all().values_list('data_source', flat=True).distinct()),
            'campaign': list(AdvertisingData.objects.all().values_list('campaign', flat=True).distinct()),
        }

    def get_filtered_queryset(self):
        queryset = AdvertisingData.objects.all()
        for filter_name in self.filters_name:
            filters = self.request.GET.getlist(filter_name)
            if filters:
                kwargs = {'{}__in'.format(filter_name): filters}
                queryset = queryset.filter(**kwargs)
        return queryset
