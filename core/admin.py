from django.contrib import admin
from core.models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ('priority', 'text')
    search_fields = ('text', 'id')
    list_filter = ('priority',)
    readonly_fields = ('priority', 'text')

    # def has_delete_permission(self, request, obj=None):
    #     return False


admin.site.register(Todo, TodoAdmin)
