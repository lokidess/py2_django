from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _

from core.forms import PostAdmin
from core.models import Post, Tag, MyUser


class MyUserAdmin(UserAdmin):
    fieldsets = (
        (None, {
            'fields': ('username', 'password')}),
        (_('Personal info'), {
            'fields': ('first_name', 'last_name', 'email', 'phone')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {
            'fields': ('last_login', 'date_joined')}),
    )


class PostAdminClass(admin.ModelAdmin):

    form = PostAdmin


admin.site.register(MyUser, MyUserAdmin)
admin.site.register(Post, PostAdminClass)
admin.site.register(Tag)
