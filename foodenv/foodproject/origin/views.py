from django.shortcuts import render_to_response
# Create your views here.
from .models import Origin

def origin(request):
	context = Origin.objects.all()
	return render_to_response('origin.html',locals())
