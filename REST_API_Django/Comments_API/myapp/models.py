from django.db import models

# Create your models here.

class Comments(models.Model):
	name = models.CharField(max_length = 100,blank = True)
	email = models.EmailField(max_length = 100,blank = True)
	body = models.TextField(max_length = 100,blank = True)

	def __str__(self):
		return self.name