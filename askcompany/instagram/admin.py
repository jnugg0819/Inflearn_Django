from django.contrib import admin
from .models import Post
# Register your models here.


@admin.register(Post)  # Wrapping
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'message', 'created_at',
                    'message_length', 'is_public', 'updated_at']
    list_display_links = ['message']
    list_filter = ['created_at', 'is_public']
    search_fields = ['message']  # message fields로 검색을 추가하겠다

    def message_length(self, post):
        return f"{len(post.message)} 글자"
