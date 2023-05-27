from django.db import models
import uuid


# Create your models here.
class Event(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, null=False)
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    Time = models.DateTimeField(null=True, blank=True)
    image = models.ImageField(upload_to='events/', default="event/event.png", null=True, blank=True)
    # likes = models.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
