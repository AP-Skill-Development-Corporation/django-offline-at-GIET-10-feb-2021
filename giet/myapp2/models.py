from django.db import models
from PIL import Image
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver 

# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	image = models.ImageField(default = 'default.jpg',upload_to='userpics')
	age = models.IntegerField(default=18)
@receiver(post_save,sender=User)
def createprofile(sender,instance,created,**kwargs):
	if created:
		UserProfile.objects.create(user=instance)


class Student(models.Model):
	Gender_choices=[('Female','Female'),('Male','Male')]
	FullName=models.CharField(max_length=30)
	RollNo=models.CharField(max_length=10)
	EmailId=models.EmailField()
	MobileNo=models.CharField(max_length=10)
	Gender=models.CharField(max_length=6,choices=Gender_choices)
	date_of_birth=models.DateField(null=True,blank=True)
	Address=models.TextField(null=True,blank=True)

	def __str__(self):
		return self.FullName

class Registration(models.Model):
	Username = models.CharField(max_length=20)
	Email = models.EmailField()
	Password = models.CharField(max_length=10)
	Image = models.ImageField(upload_to='userpics/')