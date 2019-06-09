from __future__ import unicode_literals
from django.shortcuts import render,render_to_response
# Create your views here.
from .models import Store_list
from django.shortcuts import redirect


import json

def store_showpost(request,name):
	try:
		post = Store_list.objects.get(name = name)

		if post != None:
			return render(request,'post.html',locals())
	except:
		return redirect('/')

def store_list(request):
	stores = Store_list.objects.all()
	List = []
	for i in stores:
		if None != i.vegetable:
			List.append(i.vegetable)
		else:
			List.append(None)

	
	#return render_to_response('store_list/list.html',locals())	
	return render(request,'store_list.html',locals())


