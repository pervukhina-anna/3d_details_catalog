from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return request.method in permissions.SAFE_METHODS

class IsOperatorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'operator' or request.user.is_superuser:
            return True
        return request.method in permissions.SAFE_METHODS

class IsUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.user or request.user.is_superuser:
            return True
        return request.method in permissions.SAFE_METHODS