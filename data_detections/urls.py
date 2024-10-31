from django.urls import path
from data_detections.views import ListCreateData_DetectionView, RetrieveUpdateDestroyData_DetectionView

urlpatterns = [
    path('datas/<int:arduino_id>/', ListCreateData_DetectionView.as_view()),
    path('datas-by-arduino/<int:arduino_id>/', RetrieveUpdateDestroyData_DetectionView.as_view())
]
