from django.contrib import admin
from .models import Post, Comment, Tag
from django.utils.safestring import mark_safe
# Register your models here.


@admin.register(Post)  # Wrapping
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo_tag', 'message', 'created_at',
                    'message_length', 'is_public', 'updated_at']
    list_display_links = ['message']
    list_filter = ['created_at', 'is_public']
    search_fields = ['message']  # message fields로 검색을 추가하겠다

    def photo_tag(self, post):
        if(post.photo):
            return mark_safe(f'<img src="{post.photo.url}" style="width: 72px;"/>')
        return None

    def message_length(self, post):
        return f"{len(post.message)} 글자"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
