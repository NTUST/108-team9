from django.shortcuts import render_to_response
# Create your views here.
from .models import Concept

def concept(request):
	content = Concept.objects.all()
	return render_to_response('concept.html',locals())
