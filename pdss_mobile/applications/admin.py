from django.contrib import admin

# Register your models here.
from .models import App


class AppAdmin(admin.ModelAdmin):
    list_display = ('name', 'version', 'released_at')


admin.site.register(App, AppAdmin)