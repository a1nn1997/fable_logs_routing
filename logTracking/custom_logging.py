import logging
import os

class FileSizeLimitHandler(logging.FileHandler):
    def __init__(self, filename, mode='a', maxBytes=5*1024*1024, trigger_function=None):
        super().__init__(filename, mode)
        self.maxBytes = maxBytes
        self.trigger_function = trigger_function

    def emit(self, record):
        super().emit(record)
        if self.trigger_function and os.path.getsize(self.baseFilename) >= self.max_size_bytes:
            self.trigger_function()