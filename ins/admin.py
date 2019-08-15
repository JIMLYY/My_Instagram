from django.contrib import admin

# Register your models here.
from ins.models import Post, InsUser, Like, UserConnection
admin.site.register(Post)
admin.site.register(InsUser)
admin.site.register(Like)
admin.site.register(UserConnection)
