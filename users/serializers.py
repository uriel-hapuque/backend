from rest_framework.serializers import ModelSerializer
from users.models import User 
from rest_framework import serializers


class UserSerializer(ModelSerializer):
    name = serializers.CharField(source='username')
    class Meta:
        model=User
        fields=["id", "name", "email", "date_joined", "is_superuser", "password"]
        extra_kwargs={
            "email": {"required": True},
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
    def update(self, instance, validated_data):
        for k, v in validated_data.items():
            if k == "password":
                instance.set_password(v)
                continue
            setattr(instance, k, v)
        instance.save()
        return instance