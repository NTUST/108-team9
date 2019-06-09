from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Origin(models.Model):
	text = models.CharField(max_length=2000)
	image = models.ImageField(null=True, blank=False)
	def __str__(self):
		return self.text


