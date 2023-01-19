from django.contrib import admin
from .models import Brand


class BrandAdmin(admin.ModelAdmin):
    list_display = ("name", "biography")
    ordering = ("biography",)


admin.site.register(Brand, BrandAdmin)