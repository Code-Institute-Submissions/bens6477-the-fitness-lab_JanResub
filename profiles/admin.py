from django.contrib import admin
from .models import UserProfile, Newsletter


class UserProfileAdmin(admin.ModelAdmin):

    readonly_fields = ('user', 'default_phone_number',
                       'default_address_line1', 'default_address_line2',
                       'default_city', 'default_county',
                       'default_country', 'default_postcode')

    fields = ('user', 'default_phone_number',
              'default_address_line1', 'default_address_line2',
              'default_city', 'default_county',
              'default_country', 'default_postcode')

    list_display = ('user', 'default_phone_number', 'default_country')

    ordering = ('-user',)


class NewsletterAdmin(admin.ModelAdmin):

    readonly_fields = ('user',)

    fields = ('user', 'email', 'is_registered')

    list_display = ('user', 'email', 'is_registered')

    ordering = ('-user',)


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Newsletter, NewsletterAdmin)

