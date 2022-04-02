from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'username', 'email', 'first_name',
                    'last_name', 'email', 'role', 'bio'
                    )
    search_fields = ('text',)
    #  list_filter = ('username',)
    # list_editable = ('role',)
    empty_value_display = '-пусто-'


admin.site.register(User, UserAdmin)
