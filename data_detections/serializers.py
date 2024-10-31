from rest_framework.serializers import ModelSerializer
from data_detections.models import Data_Detection

class Data_DetectionSerializer(ModelSerializer):
    class Meta:
        model=Data_Detection
        fields="__all__"
        extra_kwargs={
            "arduino": {"read_only": True}
        }
        