from django.contrib import admin
from .models import UserProfile


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


admin.site.register(UserProfile)
