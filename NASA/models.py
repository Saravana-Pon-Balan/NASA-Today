from django.db import models
class store(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	url = models.CharField(max_length=300, default="")
	
	def __str__(self):
		return self.title

