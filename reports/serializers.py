from rest_framework.serializers import ModelSerializer
from reports.models import Report

class ReportSerializer(ModelSerializer):
    class Meta:
        model=Report
        fields="__all__"
        extra_kwargs={
            "user": {"read_only": True}
        }
        