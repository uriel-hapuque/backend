from django.db import models
from users.models import User

class Arduino(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
