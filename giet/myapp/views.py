from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def static(request):
	return HttpResponse("<center><h1 style='background-color:orange;margin-left:350;margin-right:350;padding:10;border-radius:10px;'>This is static page</h1></center>")

def dynamicstr(request,name):
	return HttpResponse("<center><h3>Hii "+name+"<br>This is dynamic string url</h3></center>")	

def dynamicint(request,id):
	return HttpResponse("<center><h3>Hii {}<br>This is dynamic integer url</h3></center>".format(id))	

def dynamic(request,n,rlno):
	return HttpResponse("<center><h3>Hi {}<br>Your Rollno: {}<br>This is dynamic url".format(n,rlno))