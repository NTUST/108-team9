# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Store_list(models.Model):
    name = models.CharField(null=True,max_length=20)
    image = models.ImageField(null=True, blank=False)
    text = models.CharField(null=True,max_length=200)
    hash_tag =  models.CharField(null=True,blank=True,max_length=20)
    sub_image = models.ImageField(null=True, blank=False)
    vegetable = models.BooleanField(default=False)
    

    def __str__(self):
        return self.name
