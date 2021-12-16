from django.contrib import admin

# Register your models here.

from .models import Categoria, Comentario, Post

admin.site.register(Categoria)
admin.site.register(Post)
admin.site.register(Comentario)
