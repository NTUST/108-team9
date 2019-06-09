# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Origin


class OriginAdmin(admin.ModelAdmin):
	list_display = ('text','image')

admin.site.register(Origin)