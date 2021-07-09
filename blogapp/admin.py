from django.contrib import admin
from .models import Post


# Faz o registro o Post para ser acessado pela interface de admin
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "author", "created", "updated")
    prepopulated_fields = {"slug": ("title",)}
