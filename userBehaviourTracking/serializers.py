from rest_framework import serializers

from logTracking.models import UserLogs

class UserLogsSerializer(serializers.Serializer):
    class Meta:
        model = UserLogs
        fields = [field.name for field in model._meta.get_fields()]