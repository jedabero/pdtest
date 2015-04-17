from django.db import models


class Question(models.Model):
	"""docstring for Question"""
	question_text = models.CharField(max_lenght=200)
	pub_date = models.DateTimeField('date published')

class Choice(models.Model):
	"""docstring for Choice"""
	question = models.ForeingKey(Question)
	choice_text = models.CharField(max_lenght=200)
	votes = models.IntegerField(default=0)
		
# Create your models here.
