from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.

# admin.site.register(User)
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):

#     list_display = ('email','is_active','is_superuser','is_staff')
#     list_filter = ('is_superuser',)
#     empty_value_display = "-empty-"
#     readonly_fields = ('created_date','updated_date')
#     fields = ('email','password','is_active','is_staff','is_superuser','created_date','updated_date')
#     search_fields = ('email',)

# admin.site.register(User,UserAdmin)

class CustomUserAdmin(UserAdmin):

    models = User
    list_display = ('email','is_active','is_staff','is_superuser')
    list_filter = ('is_superuser',)
    search_fields = ('email',)
    ordering = ('-created_date',)
    fieldsets = (
        ('Authentication',{
            'fields':(
                'email','password'
            )
        }),
        ('Permissions',{
            'fields':(
                'is_active','is_staff','is_superuser',
            )
        }),
        ('Group Permissions',{
            'fields':(
                'groups','user_permissions'
            )
        }),
        ('Importants Dates',{
            'fields':(
                'last_login',
            )
        })
    )
    add_fieldsets = (
        (None,{
            'classes':('wide',),
            'fields':('email','password1','password2','is_active','is_staff','is_superuser')
        }),
    )


admin.site.register(User,CustomUserAdmin)