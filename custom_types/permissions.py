from rest_framework.permissions import SAFE_METHODS, BasePermission
from custom_types.models import Custom_Type


class IsCustom_TypeCreator(BasePermission):
    def has_object_permission(self, request, view, obj: Custom_Type):
        return request.user == obj.user

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS