from django.db import models

class News(models.Model):
	title = models.CharField(max_length = 200, verbose_name = 'Название статьи')
	content = models.TextField(blank = True, verbose_name = 'Контент статьи')
	pub_date = models.DateTimeField(auto_now_add = True, verbose_name = 'Дата публикации')
	update_date = models.DateTimeField(auto_now = True)
	preview_photo = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True)
	is_published = models.BooleanField(default = True)
	category = models.ForeignKey('Category',on_delete = models.PROTECT, null = True, verbose_name = 'Категория')

	def __str__(self):
		return (self.title)

	class Meta:
		verbose_name = 'Новость'
		verbose_name_plural = 'Новости'
		ordering= ['-pub_date']

class Category(models.Model):
	title = models.CharField(max_length = 150, db_index = True, verbose_name = 'Название категории')

	def __str__(self):
		return(self.title)

	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'
		ordering = ['title']
