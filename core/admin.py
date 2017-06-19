from django.contrib import admin
from .models import News, NewsCatcher,NewsImage, NewsCategory, NewsType
from modeltranslation.admin import TranslationAdmin

class NewsCategoryAdmin(TranslationAdmin):
	pass

class NewsTypeAdmin(TranslationAdmin):
	pass

class NewsAdmin(admin.ModelAdmin):
	pass

class NewsCatcherAdmin(admin.ModelAdmin):
	pass

class NewsImageAdmin(admin.ModelAdmin):
	pass


admin.site.register(News,NewsAdmin)
admin.site.register(NewsCatcher,NewsCatcherAdmin)
admin.site.register(NewsImage,NewsImageAdmin)
admin.site.register(NewsCategory, NewsCategoryAdmin)
admin.site.register(NewsType, NewsTypeAdmin)