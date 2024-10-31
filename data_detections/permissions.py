from rest_framework.permissions import SAFE_METHODS, BasePermission

from data_detections.models import Data_Detection


class IsData_DetectionOwner(BasePermission):
    def has_object_permission(self, request, view, obj: Data_Detection):
        return request.user == obj.user

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS