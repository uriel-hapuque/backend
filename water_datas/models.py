from django.db import models
from data_detections.models import Data_Detection


class Water_Data(models.Model):
    id=models.BigAutoField(primary_key=True)
    water_level=models.FloatField()
    dissolved_solids=models.FloatField()
    data_detection=models.OneToOneField(
        Data_Detection,
        on_delete=models.CASCADE
    )

