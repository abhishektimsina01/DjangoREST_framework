from django.db import models
from django.utils import timezone
import uuid

# todo model
class Todos(models.Model):
    id = models.UUIDField(primary_key= True, default= uuid.uuid4)
    todo = models.CharField(max_length=20)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)    

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=25)
    age = models.IntegerField()

