from arduinos.serializers import ArduinoSerializer
from arduinos.models import Arduino
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from arduinos.permissions import IsArduinoOwner, ReadOnly

class ListCreateArduinoView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Arduino.objects.all()
    serializer_class = ArduinoSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class RetrieveUpdateDestroyArduinoView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsArduinoOwner | ReadOnly]
    queryset=Arduino.objects.all()
    serializer_class=ArduinoSerializer
    lookup_url_kwarg='arduino_id'

