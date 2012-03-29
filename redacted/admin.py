from django.contrib import admin
from redacted.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_posted')

admin.site.register(Post, PostAdmin)