from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(admin.ModelAdmin):
	list_display = ('email', 'username','date_joined')
	#fields = ('email', 'username')
	fieldsets = (
		('Personal Data', {
			'fields': ('email', 'username', 'first_name','last_name','date_of_birth')
			}),
		('Bezider Data', {
			'fields': ('self_description', 'points','rank'),
		}),
		('Django Data', {
			'fields': ('is_superuser','is_active','groups','user_permissions','last_login'),
		}),
	)


admin.site.register(User, CustomUserAdmin)