from rest_framework import permissions


class IsUniversityStaff(permissions.BasePermission):
    message = 'Se requiere un rol universitario válido para acceder a este recurso.'

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        if request.user.is_staff:
            return True
        valid_roles = ['Administrador', 'Gestor', 'Auditor', 'Docente']
        return request.user.groups.filter(name__in=valid_roles).exists()
