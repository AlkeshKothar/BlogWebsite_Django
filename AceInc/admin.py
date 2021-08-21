from django.contrib import admin
from .models import blogpost, category , author, comments


# Register your models here.


admin.site.register(category)
admin.site.register(author)
admin.site.register(blogpost)
admin.site.register(comments)