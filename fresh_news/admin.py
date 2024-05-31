from django.contrib import admin

from fresh_news.models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "publish_date", )
    fields = ("title", "text", "image_url", "from_source", )
    search_fields = ("title", )
    list_filter = ("publish_date", )
    save_on_top = True
