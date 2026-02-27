from django.contrib import admin

from .models import Tarea

@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'completed', 'dateLimit')
    list_filter = ('completed', 'user')
    search_fields = ('title', 'description')
