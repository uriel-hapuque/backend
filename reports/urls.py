from django.urls import path
from reports.views import ListCreateReportView, RetrieveUpdateDestroyReportView

urlpatterns = [
    path('reports/', ListCreateReportView.as_view()),
    path('report/<int:report_id>/', RetrieveUpdateDestroyReportView.as_view())
]
