from django.db import models

class Choice(models.Model):
	
	question    = models.CharField(max_length=100)
	option1     = models.CharField(max_length=100)
	option2     = models.CharField(max_length=100)

	def __str__(self):
		return self.question


class Feedback(models.Model):
	user_id            = models.IntegerField(blank=True)
	user_name          = models.CharField(max_length=100)
	first_question     = models.CharField(max_length=100)
	first_answer       = models.CharField(max_length=100)
	second_question    = models.CharField(max_length=100)
	second_answer      = models.CharField(max_length=100)
	
	feedback_text      = models.TextField(max_length=400)

	def __str__(self):
		return self.user_name

