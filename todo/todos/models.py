from django.db import models
from time import timezone

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=200, default=None)
    #address = models.TextField(max_length=200, default=None)

    def __str__(self):
        """A string representation of the model."""
        return self.title