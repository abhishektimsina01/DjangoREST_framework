from django.contrib import admin
from .models import Todos, User, Courses, Teachers, Author, Book

# Register your models here.

admin.site.register(Todos)
admin.site.register(User)
admin.site.register(Courses)
admin.site.register(Teachers)
admin.site.register(Author)
admin.site.register(Book)