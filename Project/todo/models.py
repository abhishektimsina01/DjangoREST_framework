from django.db import models
import uuid

# todo model
class Todos(models.Model):
    id = models.UUIDField(primary_key= True, default= uuid.uuid4)
    todo = models.CharField(max_length=20)
    completed = models.BooleanField(default=False)