# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Question

class QuestionModelTests(TestCase):
	
	def test_was_published_today_with_future_question(self):
		"""
		was_published_today() should return false for future dates
		"""
		time = timezone.now() + datetime.timedelta(days=30)
		future_question = Question(pub_date=time)
		self.assertIs(future_question.was_published_today(), False)

def create_question(question_text, days):
	time = timezone.now() + datetime(timedelta(days=days))
	return Question.objects.create(question_text=question_text, pub_date=time)

def QuestionIndexViewTests(TestCase):
	def test_no_questions(self):
		response = self.client.get(reverse('polls:index'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'No polls available')
		self.assertQueryEqual(response.context['latest_question_list'], [])



