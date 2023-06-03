from django.contrib import admin

from logTracking.models import UserLogs
# Register your models here.

class UserLogsAdmin(admin.ModelAdmin):
    model = UserLogs
    list_display = [field.name for field in model._meta.get_fields()]


admin.site.register(UserLogs, UserLogsAdmin)