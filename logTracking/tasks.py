import os
from userBehaviourTracking.celery import app
from celery import shared_task
from userBehaviourTracking.utils import save_logs_and_clear_file, LOG_FILE_PATH

@app.task()
def save_data_from_file():
    save_logs_and_clear_file()

@app.task()
def save_data_from_file_when_max_size_crossed():
    file_size = os.path.getsize(LOG_FILE_PATH)
    if file_size >= 10 * 1024 * 1024:
        save_logs_and_clear_file()

    