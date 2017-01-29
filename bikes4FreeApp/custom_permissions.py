from rest_framework import permissions

class estaDeshabilitado(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.is_active:
            return True
        else:
            return False