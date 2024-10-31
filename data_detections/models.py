from django.db import models
from custom_types.models import Custom_Type
from regions.models import Region
from arduinos.models import Arduino

class Data_Detection(models.Model):
    id=models.BigAutoField(primary_key=True)
    address=models.CharField(max_length=255)
    date=models.DateTimeField(auto_now_add=True, null=True)
    type=models.ForeignKey(
        Custom_Type,
        on_delete=models.CASCADE
    )
    region=models.ForeignKey(
        Region,
        on_delete=models.CASCADE
    )
    arduino=models.ForeignKey(
        Arduino,
        on_delete=models.CASCADE
    )
