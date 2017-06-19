from django.contrib.gis.db import models
from django.conf import settings
from core.models import News, NewsCatcher
# Create your models here.

class Comment(models.Model):
	owner    = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	news     = models.ForeignKey(News, on_delete=models.CASCADE)	
	content  = models.TextField(blank=False)
	date     = models.DateTimeField(auto_now=False,auto_now_add=True)
	location = models.PointField(default=None,blank=True,null=True)
	def __str__(self):
		return '%s comment on \"%s\"' %(self.owner.username,self.news.title)

class Comment2Comment(models.Model):
	owner    = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	comment  = models.ForeignKey(Comment, on_delete=models.CASCADE)	
	content  = models.TextField(blank=False)
	date     = models.DateTimeField(auto_now=False,auto_now_add=True)
	location = models.PointField(default=None,blank=True,null=True)
	def __str__(self):
		return '%s comment to %s on \"%s\"' %(self.owner.username,self.comment.owner.username, self.comment.news.title)

class Like(models.Model):
	user    = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	news    = models.ForeignKey(News, on_delete=models.CASCADE)
	def __str__(self):
		return '%s likes \"%s\"' %(self.user.username, self.news.title)

class FollowingUser(models.Model):
	follower    = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='follower')
	followed    = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='followed')
	date        = models.DateTimeField(auto_now=False,auto_now_add=True)
	min         = models.IntegerField(default=0)
	def __str__(self):
		return '%s is following to \"%s\"' %(self.follower.username, self.followed.username)

class FollowingNews(models.Model):
	follower    = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	news        = models.ForeignKey(News, on_delete=models.CASCADE)	
	date        = models.DateTimeField(auto_now=False,auto_now_add=True)
	def __str__(self):
		return '%s is following \"%s\"' %(self.follower.username, self.news.title)

class FollowingCatcher(models.Model):
	follower    = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	catcher     = models.ForeignKey(NewsCatcher, on_delete=models.CASCADE)	
	date        = models.DateTimeField(auto_now=False,auto_now_add=True)
	min         = models.IntegerField(default=0)
	def __str__(self):
		return '%s is following \"%s\"' %(self.follower.username, self.catcher.name)