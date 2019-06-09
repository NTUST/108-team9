from __future__ import unicode_literals

from django.contrib import admin
from .models import Store_list


class Store_listAdmin(admin.ModelAdmin):
	list_display = ('name','image','text','hash_tag','sub_image','vegetable')

admin.site.register(Store_list)