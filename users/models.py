
from django.db import models
from datetime import datetime

class CustomUser(models.Model):

	username     = models.CharField(max_length=40)
	password     = models.CharField(max_length=40)
	first_name   = models.CharField(max_length=40)
	last_name    = models.CharField(max_length=40)
	email        = models.CharField(max_length=80)
	is_active    = models.BooleanField(default=True)
	is_staff     = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	last_login   = models.DateTimeField(auto_now_add=True)
	date_joined  = models.DateTimeField(default = datetime.now, blank = True)

	def __str__(self):
		return self.username


