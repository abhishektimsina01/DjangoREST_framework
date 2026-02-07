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


class Courses(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=15)
    hours = models.IntegerField()

class Teachers(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20)
    course_id = models.OneToOneField(Courses, on_delete=models.CASCADE)

class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=20)

class Book(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4)
    name = models.CharField(max_length=20)
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)