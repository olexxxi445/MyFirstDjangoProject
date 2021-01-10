from django.db import models

class Req(models.Model):
	name = models.CharField(max_length= 100, verbose_name = 'имя')
	email = models.EmailField(max_length = 100)
	phone = models.CharField(max_length = 50, verbose_name = 'телефон')


	def __str__(self):
		return self.name


	class Meta:
		verbose_name = 'Заявка'
		verbose_name_plural = 'Заявки'