from rest_framework.permissions import BasePermission,SAFE_METHODS
class permission (BasePermission):
    def has_permission(self, request, view):
        if request.Method in SAFE_METHODS:
            return True
        else:
            return request.user.is_staff
