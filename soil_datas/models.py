from django.db import models
from data_detections.models import Data_Detection

class Soil_Data(models.Model):
    id=models.BigAutoField(primary_key=True)
    soil_humidity=models.FloatField()
    data_detection=models.OneToOneField(
        Data_Detection,
        on_delete=models.CASCADE
    )

