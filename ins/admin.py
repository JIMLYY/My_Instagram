from django.contrib import admin

# Register your models here.
from ins.models import Post, InsUser, Like
admin.site.register(Post)
admin.site.register(InsUser)
admin.site.register(Like)