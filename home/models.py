# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class user(models.Model):
	name = models.CharField(max_length=30)

class troubles(models.Model):
	nickname = models.CharField(max_length=30)
	title = models.CharField(max_length=200)
	content = models.TextField(blank=False)

	def __str__(self):
		return self.title
