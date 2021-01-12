from django.contrib import admin
from .models import Post

# admin page 출력되는 내용을 customize
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'count_text']
    list_display_links = ['title']

    def count_text(self, obj):
        return '{}글자'.format(len(obj.text))



admin.site.register(Post, PostAdmin)
