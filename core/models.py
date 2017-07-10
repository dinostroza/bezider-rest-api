from django.contrib.gis.db import models
from django.conf import settings
from .managers import NewsQuerySet

def newsgategory_upload_location(instance,filename):
	return "newsgategory/%s/%s" %(instance.id,filename)

def newstype_upload_location(instance,filename):
	return "newstype/%s/%s" %(instance.id,filename)

def news_upload_location(instance,filename):
	return "news/%s/%s" %(instance.id,filename)

def news_image_upload_location(instance,filename):
	return "news/%s/%s" %(instance.id,filename)


class NewsCategory(models.Model):
	name          = models.CharField(max_length=64,unique=True,blank=False)
	description   = models.CharField(max_length=256,blank=False)
	tip           = models.CharField(max_length=128,blank=False)
	date          = models.DateTimeField(auto_now=False,auto_now_add=True)
	news_count    = models.IntegerField(default=0)
	image         = models.ImageField(upload_to=newsgategory_upload_location,null=True,blank=True)

	class Meta:
		verbose_name = 'news category'
		verbose_name_plural = 'news categories'
	def __str__(self):
		return self.name

class NewsType(models.Model):
	name        = models.CharField(max_length=64,unique=True,blank=False)
	description = models.CharField(max_length=256,blank=False)
	tip         = models.CharField(max_length=128,blank=False)
	category    = models.ForeignKey(NewsCategory,blank=False,null=True, on_delete=models.SET_NULL)
	date        = models.DateTimeField(auto_now=False,auto_now_add=True)
	news_count  = models.IntegerField(default=0)

	image       = models.ImageField(upload_to=newstype_upload_location,null=True,blank=True)

	def __str__(self):
		return self.name

class News(models.Model):
	user          = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='news', null=True, on_delete=models.SET_NULL)
	type          = models.ForeignKey(NewsType,related_name='news', on_delete=models.PROTECT)
	title         = models.CharField(max_length=64,blank=False)
	content       = models.CharField(max_length=256,blank=True)
	date          = models.DateTimeField(auto_now=False,auto_now_add=True)
	location      = models.PointField(default=None,blank=True,null=True)
	life          = models.IntegerField(default=100)
	num_visit     = models.IntegerField(default=0)
	num_share     = models.IntegerField(default=0)
	is_active     = models.BooleanField(default=True)
	
	connections   = models.ManyToManyField(
			'self'
		)

	#Social Relation Fields
	followers     = models.ManyToManyField(
			settings.AUTH_USER_MODEL,
			through='social.FollowingNews',
			through_fields=('news','follower'),
			related_name='followed_news'
		)

	likers        = models.ManyToManyField(
			settings.AUTH_USER_MODEL,
			through='social.Like',
			through_fields=('news','user'),
			related_name='liked_news'
		)

	witnesses     = models.ManyToManyField(
			settings.AUTH_USER_MODEL,
			through='social.Witness',
			through_fields=('news','user'),
			related_name='witnessed_news'
		)

	#captors
	bookmark_users = models.ManyToManyField(
			settings.AUTH_USER_MODEL,
			through='social.Bookmark',
			through_fields=('news','user'),
			related_name='bookmarks'
		)


	objects=NewsQuerySet.as_manager()

	@property
	def num_followers(self):
		return self.followers.count()

	@property
	def follower_username_list(self):
		usernames = []
		for obj in self.followers.all():
			usernames.append(obj.username)
		return usernames

	@property
	def follower_id_list(self):
		ids = []
		for obj in self.followers.all():
			ids.append(obj.id)
		return ids

	@property
	def num_likes(self):
		return self.likes.count()
		#return News.objects.filter(owner=self.id).count()

	@property
	def liker_username_list(self):
		usernames = []
		for obj in self.likers.all():
			usernames.append(obj.username)
		return usernames

	@property
	def liker_id_list(self):
		ids = []
		for obj in self.likers.all():
			ids.append(obj.id)
		return ids

	@property
	def num_witnesses(self):
		return self.witnesses.count()
		#return News.objects.filter(owner=self.id).count()

	@property
	def num_comments(self):
		return self.comments.count()

	@property
	def num_bookmarks(self):
		return self.bookmark_users.count()

	@property
	def num_images(self):
		return self.images.count()

	@property
	def latitude(self):
		return self.location.y

	@property
	def longitude(self):
		return self.location.x

	class Meta:
		verbose_name = 'news'
		verbose_name_plural = 'news'

	def __str__(self):
		return self.title

class NewsCatcher(models.Model):
	user        = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,null=True,related_name='catchers',related_query_name='catcher')
	name        = models.CharField(max_length=64,unique=True,blank=False)
	description = models.CharField(max_length=256,blank=True)
	area        = models.PolygonField(blank=False)
	location    = models.PointField(blank=True,null=True)
	date        = models.DateTimeField(auto_now=False,auto_now_add=True)

	followers   = models.ManyToManyField(
		settings.AUTH_USER_MODEL,
		through='social.FollowingCatcher',
		through_fields=('catcher','follower'),
		related_name='followed_catcher'
	)
	
	@property
	def actives_news(self):
		return News.objects.actives().filter(location__in=self.polygonField)
		#return News.objects.filter(owner=self.id).count()

	@property
	def latitude(self):
		return self.location.y

	@property
	def longitude(self):
		return self.location.x

	def __str__(self):
		return self.name

class NewsImage(models.Model):
	user        = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,null=True,related_name='images',related_query_name='image')
	news        = models.ForeignKey(News, on_delete=models.SET_NULL, null=True, related_name='images', related_query_name='image')
	image       = models.ImageField(upload_to=news_image_upload_location,null=True,blank=True)
	date        = models.DateTimeField(auto_now=False,auto_now_add=True)
	description = models.CharField(max_length=256,blank=True)
	location    = models.PointField(blank=True,null=True)

	@property
	def latitude(self):
		return self.location.y

	@property
	def longitude(self):
		return self.location.x

	def __str__(self):
		return str(self.id)