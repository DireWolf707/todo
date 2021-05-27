from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
    search_fields = ('user__username',)
admin.site.register(Todo,TodoAdmin)