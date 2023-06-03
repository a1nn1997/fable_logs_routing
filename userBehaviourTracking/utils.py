import json

import logging
from rest_framework import status as drf_response_status
from rest_framework.response import Response

logger = logging.getLogger("applogger")
default_logger = logging.getLogger("default")
LOG_FILE_PATH = "./logs/user_behaviour_tracking.log"

def logging_helpers(data: dict()) -> None:
     # Load existing log data from the file
    try:
        with open(LOG_FILE_PATH, "r") as file:
            log_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        log_data = []

    # Append the new data to the existing list
    log_data.append(data)

    # Save the updated data back to the file
    with open(LOG_FILE_PATH, "w") as file:
        json.dump(log_data, file)

def response(error: bool = False, message: str= "", data=None)  -> Response():
    if data is None:
        data = dict()
    status = drf_response_status.HTTP_400_BAD_REQUEST if error else drf_response_status.HTTP_201_CREATED
    body = dict(status=status,message=message, data=data)
    return Response(data=body, status=status)

def read_log_data():
    try:
        with open(LOG_FILE_PATH, "r") as file:
            log_data = json.load(file)
        return log_data
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_logs_and_clear_file():
    from logTracking.models import UserLogs
    filename = LOG_FILE_PATH

    log_data = read_log_data()
    for data in log_data:
        UserLogs.objects.create(**data)
        print("data")
    # Clear the log file
    with open(filename, "w") as file:
        pass
