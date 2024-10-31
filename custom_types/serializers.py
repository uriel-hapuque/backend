from rest_framework.serializers import ModelSerializer
from custom_types.models import Custom_Type

class Custom_TypeSerializer(ModelSerializer):
    class Meta:
        model=Custom_Type
        fields="__all__"
        extra_kwargs={
            "user": {"read_only": True}
        }
        