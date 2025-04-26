from django.contrib import admin
from django.templatetags.static import static
from django.utils.html import format_html

from .forms import BlogAdminForm
from .models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    form = BlogAdminForm
    list_display = ('title', 'short_content', 'created_at', 'view_article_link')
    search_fields = ('title', 'content')
    list_filter = ('created_at',)
    prepopulated_fields = {'slug': ('title',)}

    def short_content(self, obj):
        clean_content = obj.content
        if len(clean_content) > 100:
            return format_html(clean_content[:100] + '...')
        return format_html(clean_content)

    def view_article_link(self, obj):
        return format_html('<a href="/blogs/blog/{}/" target="_blank">مشاهده مقاله</a>', obj.id)

    short_content.short_description = 'محتوا'
    view_article_link.short_description = 'مشاهده'

    class Media:
        js = (static('js/init_tinymce.js'),)
