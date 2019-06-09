from django.shortcuts import render_to_response
# Create your views here.
from .models import History

def history(request):
	content = History.objects.all()
	return render_to_response('history.html',locals())
