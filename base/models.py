from django.db import models
import os
import random
from datetime import datetime

def get_filename_ext(filename):

	name,ext = os.path.splitext(filename)
	return ext

def upload_image_path(instance, filename):
	#print(instance)
	#print(filename)

	new_filename   = random.randint(11111111,7000000000000)
	ext            = get_filename_ext(filename)
	final_filename = f'{new_filename}{ext}'
	return f'images/{new_filename}/{final_filename}'




class Blog(models.Model):
	title        = models.CharField(max_length=300)
	summary      = models.CharField(max_length=400)
	blog         = models.TextField()
	photo        = models.ImageField(upload_to=upload_image_path)
	is_published = models.BooleanField(default=True)
	date         = models.DateTimeField(default = datetime.now)

	def __str__(self):
		return self.title

