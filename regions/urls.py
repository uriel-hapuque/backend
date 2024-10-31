from django.urls import path
from regions.views import ListCreateRegionView, RetrieveUpdateDestroyRegionView

urlpatterns = [
    path('regions/', ListCreateRegionView.as_view()),
    path('region/<int:region_id>/', RetrieveUpdateDestroyRegionView.as_view())
]
