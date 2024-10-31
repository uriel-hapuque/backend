from rest_framework.permissions import SAFE_METHODS, BasePermission
from reports.models import Report


class IsReportCreator(BasePermission):
    def has_object_permission(self, request, view, obj: Report):
        return request.user == obj.user

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS