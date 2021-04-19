from django.contrib import admin

from .models import News, Category

class NewsAdmin(admin.ModelAdmin):
	list_display = ('id','title', 'category', 'pub_date', 'is_published')
	list_display_links = ('title','id')
	search_fields = ('title', 'pub_date')
	list_editable = ('is_published',)
	list_filter = ('category','is_published')

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('id','title')
	list_display_links = ('title','id')
	search_fields = ('title',)



admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)


