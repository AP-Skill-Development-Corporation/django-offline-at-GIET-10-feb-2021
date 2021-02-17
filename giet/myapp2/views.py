from django.shortcuts import render, redirect
from django.http import HttpResponse
import random
from myapp2.models import Student,Registration,UserProfile
from myapp2.forms import StudentForm,RegisterForm
from django.contrib import messages
from giet import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
# Create your views here.
def stat(request):
	return HttpResponse("Iam from Myapp2")
def home(request):
	return HttpResponse("Iam from Myapp2 Urls")

def index(request):
	value = random.randint(1,100)
	return render(request, 'index.html',{'name':value})

def student(request):
	details = {'name':'Gopi','number':44, 'branch':'cse'}
	return render(request,"student_info.html",{'details':details})

def value(request, val):
	a = []
	for i in range(1,val+1):
		a.append(i)
	return render(request,"value.html",{'value':a})

def table(request, v):
	a = []
	for i in range(1,11):
		a.append(i*v)
	return render(request,'table.html',{'array':a,'v':v})
def sample(request):
	return render(request,'sample.html')
def register(request):
	if request.method == 'POST':
		fname = request.POST.get('fname')
		roll_number = request.POST.get('rollnum')
		email = request.POST.get('email')
		phone = request.POST.get('phone')
		gender = request.POST.get('gender')
		# context = {'fname':fname,"roll_number":roll_number,'email':email,'phone':phone, "gender":gender}
		
		Student.objects.create(FullName=fname,RollNo=roll_number,EmailId=email,MobileNo=phone,Gender=gender)
		return redirect('details')
	return render(request,'register.html')


def disply_details(request):
	data = Student.objects.all()
	return render(request,'result.html',{'data':data})


def update_details(request,id):
	data = Student.objects.get(id=id)
	if request.method == 'POST':
		data.FullName = request.POST.get('fname')
		data.RollNo = request.POST.get('rollnum')
		data.EmailId = request.POST.get('email')
		data.MobileNo = request.POST.get('phone') 
		data.Gender= request.POST.get('gender')
		data.save()
		return redirect('details')
	return  render(request,'update.html',{'data':data})


def delete(request, id):
	Student.objects.get(id=id).delete()
	return redirect('details')

def signup(request):
	if request.method=='POST':
		form=StudentForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,"Successfully Registered...!")
		return redirect('signup')
		#return HttpResponse("Successfully Registered")
	form=StudentForm()
	return render(request,"signup.html",{'form':form})

def registration(request):
	if request.method == 'POST':
		uname = request.POST.get('uname')
		email = request.POST.get('email')
		pwd = request.POST.get('pwd')
		im = request.FILES['image']
		Registration.objects.create(Username=uname,Email=email,Password=pwd,Image=im)
		sub = 'reg welcome message'
		body = 'username'+uname+'password'+pwd
		receiver = email
		sender = settings.EMAIL_HOST_USER
		send_mail(sub,body,sender,[receiver])

		return redirect('showdata')
	return render(request,'registration.html')

def showdata(request):
	data = Registration.objects.all()
	return render(request,'showdata.html',{'data':data})

def signupform(request):
	if request.method == 'POST':
		sform = RegisterForm(request.POST)
		if sform.is_valid:
			sform.save()
			return HttpResponse('Sucessfully Registered')
	else:
		sform = RegisterForm()
		return render(request,'signupform.html',{'sform':sform})

def profile(request):
	user = User.objects.get(id=request.user.id)
	pro = UserProfile.objects.get(user=user)
	return render(request,'profile.html',{'user':user,'pro':pro})




























