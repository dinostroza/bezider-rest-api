from django.contrib.gis.db import models
from django.conf import settings
from core.models import News, NewsCatcher
#from user.models import User
# Create your models here.

class Comment(models.Model):
	user    = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comments',related_query_name='comment', on_delete=models.CASCADE)
	news     = models.ForeignKey(News, related_name='comments',related_query_name='comment', on_delete=models.CASCADE)	
	content  = models.TextField(blank=False)
	date     = models.DateTimeField(auto_now=False,auto_now_add=True)
	location = models.PointField(default=None,blank=True,null=True)

	@property
	def latitude(self):
		return self.location.y

	@property
	def longitude(self):
		return self.location.x

	class Meta:
		verbose_name = 'Comment'
		verbose_name_plural = 'Comments'
	def __str__(self):
		return '%s comment on \"%s\"' %(self.owner.username,self.news.title)

class Reply(models.Model):
	user      = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='replies',related_query_name='reply', on_delete=models.CASCADE)
	comment    = models.ForeignKey(Comment, related_name='replies',related_query_name='reply',on_delete=models.CASCADE)
	content    = models.TextField(blank=False)
	date       = models.DateTimeField(auto_now=False,auto_now_add=True)
	location   = models.PointField(default=None,blank=True,null=True)

	@property
	def latitude(self):
		return self.location.y

	@property
	def longitude(self):
		return self.location.x

	class Meta:
		verbose_name = 'Reply'
		verbose_name_plural = 'Replies'
	def __str__(self):
		return '%s comment to %s on \"%s\"' %(self.owner.username,self.comment.owner.username, self.comment.news.title)

class Bookmark(models.Model):
	user    = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='bookmark_data',related_query_name='bookmark_data', on_delete=models.CASCADE)
	news    = models.ForeignKey('core.News', related_name='bookmark_data',related_query_name='bookmark_data',on_delete=models.CASCADE)

class Like(models.Model):
	user    = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='likes',related_query_name='like', on_delete=models.CASCADE)
	news    = models.ForeignKey(News,related_name='likes',related_query_name='like', on_delete=models.CASCADE)
	class Meta:
		verbose_name = 'Like'
		verbose_name_plural = 'Likes'
	def __str__(self):
		return '%s likes \"%s\"' %(self.user.username, self.news.title)

class Witness(models.Model):
	user  = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='witnesses_data',related_query_name='witness_data',on_delete=models.CASCADE)
	news  = models.ForeignKey(News,related_name='witnesses_data',related_query_name='witness_data', on_delete=models.CASCADE)
	class Meta:
		verbose_name = 'Witness'
		verbose_name_plural = 'Witnesses'
	def __str__(self):
		return '%s witness \"%s\"' %(self.user.username, self.news.title)

class FollowingUser(models.Model):
	follower    = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='follower_users_data',related_query_name='follower_user_data', on_delete=models.CASCADE)
	user        = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='followed_users_data',related_query_name='followed_user_data', on_delete=models.CASCADE)
	date        = models.DateTimeField(auto_now=False,auto_now_add=True)
	min         = models.IntegerField(default=0)
	class Meta:
		verbose_name = 'Following User'
		verbose_name_plural = 'Following Users'
	def __str__(self):
		return '%s is following to \"%s\"' %(self.follower.username, self.followed.username)

class FollowingNews(models.Model):
	follower    = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='following_news_data',related_query_name='following_news_data', on_delete=models.CASCADE)
	news        = models.ForeignKey(News,related_name='following_news_data',related_query_name='following_news_data', on_delete=models.CASCADE)	
	date        = models.DateTimeField(auto_now=False,auto_now_add=True)
	class Meta:
		verbose_name = 'Following News'
		verbose_name_plural = 'Following News'
	def __str__(self):
		return '%s is following \"%s\"' %(self.follower.username, self.news.title)

class FollowingCatcher(models.Model):
	follower    = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='following_catcher_data',related_query_name='following_catcher_data', on_delete=models.CASCADE)
	catcher     = models.ForeignKey(NewsCatcher,related_name='following_catcher_data',related_query_name='following_catcher_data', on_delete=models.CASCADE)	
	date        = models.DateTimeField(auto_now=False,auto_now_add=True)
	min         = models.IntegerField(default=0)
	class Meta:
		verbose_name = 'Following Catcher'
		verbose_name_plural = 'Following Catchers'
	def __str__(self):
		return '%s is following \"%s\"' %(self.follower.username, self.catcher.name)
		