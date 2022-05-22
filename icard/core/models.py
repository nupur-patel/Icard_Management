from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class College(models.Model):
	college_name = models.CharField(max_length = 200)
	color = models.CharField(max_length = 7)  # Hex value can be only 6 digit
	def __str__(self):
		return self.college_name

class Student(models.Model):
	college = models.ForeignKey(College, on_delete=models.CASCADE)
	first_name = models.CharField(null = False,blank = False, max_length = 100)	# required
	last_name = models.CharField(null = False,blank = False,max_length = 100) #required
	address = models.TextField(null = False,blank = False,max_length = 500)   #required
	dob = models.DateField(null = False,blank = False,)						#required
	division = models.CharField(max_length = 20) 	
	year = models.PositiveSmallIntegerField(blank=True, null=True)				#	
	phone = PhoneNumberField(unique = True, null = False)		# Read documentation and Django phonenumber field
	photo = models.ImageField(upload_to = "icard-images", height_field = None, width_field = None)					# research on it.


	def __str__(self):
		return self.first_name + ' ' + self.last_name
