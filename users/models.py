from django.db import models

class User(models.Model):
	id 				= models.IntegerField(primary_key=True)
	first_name 		= models.CharField(max_length=50)
	last_name 		= models.CharField(max_length=50)
	company_name 	= models.CharField(max_length=100)
	age 			= models.IntegerField()
	city 			= models.CharField(max_length=100)
	state 			= models.CharField(max_length=100)
	zip 			= models.IntegerField()
	email 			= models.EmailField(max_length=100)
	web 			= models.CharField(max_length=100)

	def __str__(self):
		return self.first_name