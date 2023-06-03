import uuid
from django.db import models

# Create your models here.

class UserLogs(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    id = models.BigIntegerField(unique=False)
    unix_ts = models.BigIntegerField()
    user_id = models.BigIntegerField()
    event_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"user with id {self.id}, unix_ts {self.unix_ts}, user_id {self.user_id} and event_name {self.event_name}"
    
