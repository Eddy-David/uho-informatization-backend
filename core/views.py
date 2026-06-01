from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .models import AuditLog
from .permissions import IsUniversityStaff
from .utils import register_audit_event


class StatusAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        register_audit_event(request.user, 'status_check', resource='system')
        return Response({'status': 'ok', 'message': 'API UHO operativa'})


class DashboardAPIView(APIView):
    permission_classes = [IsUniversityStaff]

    def get(self, request):
        modules = [
            'Gestión de Estudiantes',
            'Procesos Académicos',
            'Recursos Humanos',
            'Mantenimiento',
            'Investigación',
            'Analítica Universitaria',
            'Inteligencia Artificial',
        ]
        register_audit_event(request.user, 'dashboard_view', resource='dashboard')
        return Response({
            'users': 0,
            'modules': len(modules),
            'auditEvents': AuditLog.objects.count(),
            'enabledModules': modules,
        })
