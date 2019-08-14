from django.contrib import admin

# Register your models here.
from ins.models import Post, InsUser
admin.site.register(Post)
admin.site.register(InsUser)