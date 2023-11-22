from django.contrib import admin

# Register your models here.
from .models import Author, Book

classes = [Author, Book]

for model in classes:
    admin.site.register(model)
