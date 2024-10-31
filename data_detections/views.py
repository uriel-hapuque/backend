from data_detections.serializers import Data_DetectionSerializer
from data_detections.models import Data_Detection
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from data_detections.permissions import IsData_DetectionOwner, ReadOnly
import re
from arduinos.models import Arduino
from django.shortcuts import get_object_or_404

class ListCreateData_DetectionView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Data_Detection.objects.all()
    serializer_class = Data_DetectionSerializer
    def perform_create(self, serializer):
        arduino_id = id=int(re.search(r'\d+', self.request.path_info).group())
        arduino = get_object_or_404(Arduino, id=arduino_id)
    
        serializer.save(arduino=arduino)

class RetrieveUpdateDestroyData_DetectionView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsData_DetectionOwner | ReadOnly]
    queryset=Data_Detection.objects.all()
    serializer_class=Data_DetectionSerializer
    lookup_url_kwarg='arduino_id'

