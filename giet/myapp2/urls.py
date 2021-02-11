from django.urls import path
from myapp2 import views
urlpatterns = [
	path('homeurl/',views.home,name="home"),
]