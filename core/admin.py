from django.contrib import admin

from .models import Autor, Post, User

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Post, PostAdmin)
admin.site.register(Autor)
admin.site.register(User)





