from django.db import models
from users.models import User

class Region(models.Model):
    id = models.BigAutoField(primary_key=True)
    street = models.CharField(max_length=255, unique=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    
