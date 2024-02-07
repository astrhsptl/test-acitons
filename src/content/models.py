from uuid import uuid4
from django.db import models


class Notification(models.Model):
    id = models.UUIDField(
        primary_key=True,
        db_index=True,
        default=uuid4,
        editable=False
    )
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=512, null=False, blank=False)

    def __str__(self):
        return str(self.title)
