from django.contrib import admin
from .models import Images


class imageAdmin(admin.ModelAdmin):
    list_display = ["title", "image_file", "description", "binaryimage"]


admin.site.register(Images, imageAdmin)
