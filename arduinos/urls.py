from django.urls import path
from arduinos.views import ListCreateArduinoView, RetrieveUpdateDestroyArduinoView

urlpatterns = [
    path('arduinos/', ListCreateArduinoView.as_view()),
    path('arduino/<int:arduino_id>/', RetrieveUpdateDestroyArduinoView.as_view())
]
