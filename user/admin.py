from django.contrib import admin
#from django.contrib.auth.admin import UserAdmin
from .models import User, Superuser, Staffuser


class CustomUserAdmin(admin.ModelAdmin):
	list_display = ( 'username','email','is_staff','date_joined')
	#fields = ('email', 'username')

	fieldsets = (
		('Personal Data', {
			'fields': ('email', 'username', 'first_name','last_name','date_of_birth')
			}),
		('Bezider Data', {
			'fields': ('self_description', 'points','rank'),
		}),
		('Django Data', {
			'fields': ('is_active','groups','user_permissions','last_login'),
		}),
	)

	def is_staff(self, obj):
		return obj.is_staff

	is_staff.boolean=True
	is_staff.short_description='Staff/Superuser Status'

class SuperuserAdmin(admin.ModelAdmin):
	list_display = ( 'user',)

class StaffuserAdmin(admin.ModelAdmin):
	list_display = ( 'user',)

admin.site.register(User, CustomUserAdmin)
admin.site.register(Superuser, SuperuserAdmin)
admin.site.register(Staffuser, StaffuserAdmin)