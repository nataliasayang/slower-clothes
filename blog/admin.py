from django.contrib import admin
from .models import Post, PostImage

class PostImageAdmin(admin.StackedInline):
    model = PostImage

admin.site.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
       model = Post

admin.site.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass
