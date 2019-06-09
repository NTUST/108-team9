from __future__ import unicode_literals

from django.contrib import admin
from .models import Concept


class ConceptAdmin(admin.ModelAdmin):
	list_display = ('text')

admin.site.register(Concept)