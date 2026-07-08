from django.contrib import admin
from .models import TODO

@admin.register(TODO)
class TodoAdmin(admin.ModelAdmin):
    model = TODO
    list_display = ('date', 'body', 'done')


