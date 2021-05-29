import uuid
import datetime
from django.db import models


class unique_field(models.Model):
    uu_id = models.UUIDField(default=uuid.uuid4, unique=True, db_index=False)
    timeStampField = models.DateTimeField(datetime.datetime, db_index=False)


