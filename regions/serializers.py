from rest_framework.serializers import ModelSerializer
from regions.models import Region

class RegionSerializer(ModelSerializer):
    class Meta:
        model=Region
        fields="__all__"
        extra_kwargs={
            "user": {"read_only": True}
        }
        