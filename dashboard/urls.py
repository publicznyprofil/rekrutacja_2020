from django.urls import path

from dashboard.views import DashboardView, DashboardJsonView

app_name = 'dashboard'

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('json', DashboardJsonView.as_view(), name='dashboard_json'),
]
