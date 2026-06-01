from .models import AuditLog


def register_audit_event(user, action, resource='', details=''):
    AuditLog.objects.create(
        user=user if hasattr(user, 'is_authenticated') and user.is_authenticated else None,
        action=action,
        resource=resource,
        details=details,
    )
