from django.db import models
<<<<<<< HEAD
class store(models.Model):
	title = models.CharField(max_length=100,unique=True)
	description = models.TextField()
	url = models.CharField(max_length=300, default="")
	
	def __str__(self):
		return self.title
=======
from django.utils import timezone

class store(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    url = models.CharField(max_length=300, default="")
    date = models.DateTimeField(default=timezone.now, editable=False)
    
    def __str__(self):
        return self.title
>>>>>>> 888e0b0 (date added)

