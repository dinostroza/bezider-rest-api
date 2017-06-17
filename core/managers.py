from django.contrib.gis.db import models
from django.core.exceptions import MultipleObjectsReturned
#from django.utils import translation
#from hvad.manager import TranslationManager, TranslationQueryset

class NewsQuerySet(models.QuerySet):
	def actives(self):
		return self.filter(is_active=True)

	def inactives(self):
		return self.filter(is_active=False)

	def type(self,name):
		return self.filter(news_type__name=name)

	def category(self,name):
		return self.filter(news_type__category__name=name)

#Experimental manager
class NewsManager(models.Manager):
	def get_queryset(self):
		return NewsQuerySet(self.model, using=self._db)

	def actives(self):
		return self.get_queryset().actives()

	def inactives(self):
		return self.get_queryset().inactives()

	def type(self,name):
		return self.get_queryset().type(name=name)