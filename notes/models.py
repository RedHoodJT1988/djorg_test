from django.db import models
from uuid import uuid4

class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    # TODO: Add user/author who created it
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    # TODO: Tagging systems or categories
