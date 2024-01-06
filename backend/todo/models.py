from django.db import models


class Todo(models.Model):
    body = models.CharField(max_length=300)
    selesai = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
