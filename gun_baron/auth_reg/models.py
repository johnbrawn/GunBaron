from django.db import models


class User(models.Model):
	login = models.EmailField()
	password = models.CharField(max_length=100)
	first_name = models.CharField(max_length=100, blank=True)
	second_name = models.CharField(max_length=100, blank=True)
	
	def __str__(self):
		return '%s %s' % (self.login, self.first_name)
