from django.urls import path
from myapp2 import views
urlpatterns = [
	path('homeurl/',views.home,name="home"),
	path('index/',views.index , name= 'index'),
	path('student',views.student, name = 'student'),
	path('<int:val>',views.value,name= 'value'),#localhost:myapp2/67
	path("table/<int:v>",views.table, name= 'table'),
]