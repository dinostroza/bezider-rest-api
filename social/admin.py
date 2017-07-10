from django.contrib import admin
from .models import *

class CommentAdmin(admin.ModelAdmin):
	pass

class ReplyAdmin(admin.ModelAdmin):
	pass

class LikeAdmin(admin.ModelAdmin):
	pass

class FollowingUserAdmin(admin.ModelAdmin):
	pass

class FollowingNewsAdmin(admin.ModelAdmin):
	pass

class FollowingCatcherAdmin(admin.ModelAdmin):
	pass

class WitnessAdmin(admin.ModelAdmin):
	pass

class BookmarkAdmin(admin.ModelAdmin):
	pass

admin.site.register(Witness,CommentAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Reply,ReplyAdmin)
admin.site.register(Like,LikeAdmin)
admin.site.register(Bookmark,BookmarkAdmin)
admin.site.register(FollowingUser,FollowingUserAdmin)
admin.site.register(FollowingNews,FollowingNewsAdmin)
admin.site.register(FollowingCatcher,FollowingCatcherAdmin)