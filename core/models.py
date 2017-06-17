from django.contrib.gis.db import models
from django.conf import settings
from .managers import NewsManager

def newsgategory_upload_location(instance,filename):
	return "newsgategory/%s/%s" %(instance.id,filename)

def newstype_upload_location(instance,filename):
	return "newstype/%s/%s" %(instance.id,filename)

def news_upload_location(instance,filename):
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
	owner         = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
	news_type     = models.ForeignKey(NewsType, on_delete=models.PROTECT)
	title         = models.CharField(max_length=64,blank=False)
	content       = models.CharField(max_length=256,blank=True)
	date          = models.DateTimeField(auto_now=False,auto_now_add=True)
	location      = models.PointField(default=None,blank=True,null=True)
	life          = models.IntegerField(default=100)
	visit_count   = models.IntegerField(default=0)
	shared_count  = models.IntegerField(default=0)
	is_active     = models.BooleanField(default=True)

	objects=NewsManager()



	def latitude(self):
		return self.location.y

	def longitude(self):
		return self.location.x

	class Meta:
		verbose_name = 'news'
		verbose_name_plural = 'news'

	def __str__(self):
		return self.title

class NewsCatcher(models.Model):
	owner       = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,null=True)
	name        = models.CharField(max_length=64,unique=True,blank=False)
	description = models.CharField(max_length=256,blank=True)
	area        = models.PolygonField(blank=False)
	location    = models.PointField(blank=True,null=True)
	date        = models.DateTimeField(auto_now=False,auto_now_add=True)
	def __str__(self):
		return self.name

class NewsImage(models.Model):
	owner       = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,null=True)
	news        = models.ForeignKey(News, on_delete=models.SET_NULL,null=True)
	image       = models.ImageField(upload_to=news_upload_location,null=True,blank=True)
	date        = models.DateTimeField(auto_now=False,auto_now_add=True)
	description = models.CharField(max_length=256,blank=True)
	location    = models.PointField(blank=True,null=True)
	def __str__(self):
		return str(self.id)