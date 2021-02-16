from myapp2.models import Student
from django import forms

class StudentForm(forms.ModelForm):
	class Meta:
		model=Student
		#fields='__all__'
		fields=['FullName','RollNo','EmailId','MobileNo','Gender']
		widgets={
		"FullName":forms.TextInput(attrs={'placeholder':'Enter FullName'}),
		"RollNo":forms.TextInput(attrs={'placeholder':'Enter RollNo'}),
		"EmailId":forms.EmailInput(attrs={'placeholder':'Enter Emailid'}),
		"MobileNo":forms.TextInput(attrs={'placeholder':'Enter MobileNo'}),

		}

