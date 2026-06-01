from django.contrib import admin
from .models import AuditLog

@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'user', 'action', 'resource')
    list_filter = ('action', 'resource')
    search_fields = ('user', 'action', 'resource', 'details')
