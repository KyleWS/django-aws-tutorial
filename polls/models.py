# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	
	def __str__(self):
		return self.question_text	

	def was_published_today(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now
	was_published_today.admin_order_field = 'pub_date'
	was_published_today.boolean = True
	was_published_today.short_description = 'Published today?'	

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text + str(self.votes)	
