from django.contrib import admin
from .models import Comment, Comment2Comment, Like, FollowingUser, FollowingNews, FollowingCatcher

class CommentAdmin(admin.ModelAdmin):
	pass

class Comment2CommentAdmin(admin.ModelAdmin):
	pass

class LikeAdmin(admin.ModelAdmin):
	pass

class FollowingUserAdmin(admin.ModelAdmin):
	pass

class FollowingNewsAdmin(admin.ModelAdmin):
	pass

class FollowingCatcherAdmin(admin.ModelAdmin):
	pass	

admin.site.register(Comment,CommentAdmin)
admin.site.register(Comment2Comment,Comment2CommentAdmin)
admin.site.register(Like,LikeAdmin)
admin.site.register(FollowingUser,FollowingUserAdmin)
admin.site.register(FollowingNews,FollowingNewsAdmin)
admin.site.register(FollowingCatcher,FollowingCatcherAdmin)