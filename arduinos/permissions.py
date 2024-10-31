from rest_framework.permissions import SAFE_METHODS, BasePermission

from arduinos.models import Arduino


class IsArduinoOwner(BasePermission):
    def has_object_permission(self, request, view, obj: Arduino):
        return request.user == obj.user

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS