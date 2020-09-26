from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


class UserExtendInline(admin.StackedInline):
    model = UserExtend
    can_delete = False
    verbose_name_plural = 'userextend'


# Register your models here.
class UserAdmin(BaseUserAdmin):
    inlines = (UserExtendInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Books)
admin.site.register(Courses)
admin.site.register(Groups)
admin.site.register(Roles)
admin.site.register(Subjects)
admin.site.register(Student)
admin.site.register(Teachers)
