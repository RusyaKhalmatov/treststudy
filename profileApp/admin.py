from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


# class ProfileInline(admin.StackedInline):
#     model = Profile
#     can_delete = False
#     verbose_name_plural = 'profile'
#
#
# # Register your models here.
# class UserAdmin(BaseUserAdmin):
#     inlines = (ProfileInline,)
#
#
# admin.site.unregister(User)
admin.site.register(Profile)
admin.site.register(Books)
admin.site.register(Course)
admin.site.register(Class)
admin.site.register(Roles)
admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Dean)
admin.site.register(Faculty)


