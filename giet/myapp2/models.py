from django.db import models

# Create your models here.
class Student(models.Model):
	Gender_choices=[('Female','Female'),('Male','Male')]
	FullName=models.CharField(max_length=30)
	RollNo=models.CharField(max_length=10)
	EmailId=models.EmailField()
	MobileNo=models.CharField(max_length=10)
	Gender=models.CharField(max_length=6,choices=Gender_choices)
	Address=models.TextField()