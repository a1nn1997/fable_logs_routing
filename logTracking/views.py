from rest_framework.views import APIView
from userBehaviourTracking.utils import logging_helpers, response
from userBehaviourTracking.serializers import UserLogsSerializer

class UserBehaviourManagement(APIView):
    def post(self, request):
        (error, message, data) = (False, "Success", request.data)
        try:
            serialized_data = UserLogsSerializer(data=data)
            serialized_data.is_valid(raise_exception=True)
            logging_helpers(data)
        except Exception as e:
            (error, message) = (True, "Failure")
            data = dict(error_type=type(e).__name__, error=str(e))
        return response(error=error, message=message, data = data)
