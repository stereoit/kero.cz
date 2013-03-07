from django.contrib import admin
import models

class NewsAdmin(admin.ModelAdmin):
    list_display = ['title','slug','published','published_by']
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(models.News, NewsAdmin)
