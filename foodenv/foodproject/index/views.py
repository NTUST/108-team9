from django.shortcuts import render_to_response,render
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponseRedirect

def Index(request):
	return render(request,'index.html',locals())

def toRank(request):
	return render(request,'rank.html',locals())

def toSignin(request):


	try:
		userid = request.GET['user_id']
		userpass = request.GET['user_pass']
		allData = User.objects.all()
	except:
		userid = None
		message = "Error"
	if userid != None and userpass != None:

		for i in allData:
			if i.email == userid and i.check_password(userpass):
				
				return render(request,'index.html',locals())
	return render(request,'signin.html',locals())

def toOrigin(request):
	return render(request,'origin.html',locals())

def toAbout_us(request):
	return render(request,'about_us.html',locals())


def toSignup(request):
	try:
		userfn = request.GET['user_fn']
		userln = request.GET['user_ln']
		useremail = request.GET['user_email']
		userpass = request.GET['user_pass']
		userpassconfirm = request.GET['user_passconfirm']
	except:
		useremail = None
		message = "Error"
	if useremail != None and userpass == userpassconfirm:
		user = User.objects.create_user(str(useremail),useremail,userpass)
		user.last_name = userln
		user.first_name = userfn
		user.save()
	return render(request,'signup.html',locals())


