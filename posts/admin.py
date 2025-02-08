from django.contrib import admin
from .models import Post, DatePost, Book, Person, Group

admin.site.register(Post)
admin.site.register(DatePost)
admin.site.register(Book)
admin.site.register(Person)
admin.site.register(Group)