from django.contrib import admin
from bloggerapp.models import *
# Register your models here.

admin.site.register(BlogUser)
admin.site.register(Blog)
admin.site.register(BlogComment)
admin.site.register(BlogLikes)