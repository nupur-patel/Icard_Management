from django.shortcuts import render,redirect
from .models import *
from django.core.files.storage import FileSystemStorage
# Create your views here.

def index(request):

	if request.method == "POST" and request.FILES:
		firstname = request.POST["firstname"]
		lastname = request.POST["lastname"]
		address = request.POST["address"]
		phone = request.POST["phone"]
		dob = request.POST["dateofbirth"]
		branch = request.POST["branch"]
		year = request.POST["year"]
		photo = request.FILES["photo"]

		id = request.POST.get("college")
		college = College.objects.get(id=id)
		#print(college)

		std = Student.objects.create(college = college, first_name = firstname, last_name = lastname, address = address, dob = dob, division = branch, year = year,phone = phone, photo = photo)
		std.save()
		return redirect("student-profile/"+ str(std.id))

	context = {}
	colleges = College.objects.all()
	context['colleges'] = colleges
	
	return render(request,template_name = 'core/register.html',context = context)

def profile(request,id):
	
	data = Student.objects.get(id = id)
	print(data)
	context = {}
	context['data'] = data

	return render(request,template_name = "core/profile.html",context=context)

















