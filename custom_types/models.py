from django.db import models
from users.models import User

class Custom_Type(models.Model):
    types_choice = [
        ("Type 1", "Type 1"),
        ("Type 2", "Type 2"),
        ("Type 3", "Type 3")
    ]
    id=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=55, choices=types_choice)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )


    