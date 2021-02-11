from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def stat(request):
	return HttpResponse("Iam from Myapp2")
def home(request):
	return HttpResponse("Iam from Myapp2 Urls")