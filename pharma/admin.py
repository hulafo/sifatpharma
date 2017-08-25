from django.contrib import admin
from pharma.models import Post

class PostModelAdmin(admin.ModelAdmin):
    list_display=["title","image","date"]
    list_display_links=["date"]
    list_editable=["title"]
    list_filter=["title"]
    search_fields=["body","title"]
    class Meta:
        model=Post
admin.site.register(Post,PostModelAdmin)
# Register your models here.
