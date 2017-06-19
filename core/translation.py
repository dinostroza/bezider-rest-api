from modeltranslation.translator import translator, TranslationOptions
from .models import NewsCategory, NewsType

class NewsCategoryTranslationOptions(TranslationOptions):
	fields = ('name', 'description','tip',)

class NewsTypeTranslationOptions(TranslationOptions):
	fields = ('name', 'description','tip',)


translator.register(NewsCategory, NewsCategoryTranslationOptions)
translator.register(NewsType, NewsTypeTranslationOptions)