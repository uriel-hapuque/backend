from rest_framework.serializers import ModelSerializer
from arduinos.models import Arduino

class ArduinoSerializer(ModelSerializer):
    class Meta:
        model=Arduino
        fields="__all__"
        extra_kwargs={
            "user": {"read_only": True}
        }
        