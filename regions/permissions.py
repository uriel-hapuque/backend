from rest_framework.permissions import SAFE_METHODS, BasePermission
from regions.models import Region


class IsRegionCreator(BasePermission):
    def has_object_permission(self, request, view, obj: Region):
        return request.user == obj.user

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS