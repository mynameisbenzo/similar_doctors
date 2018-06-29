from django.urls import path

from . import views

app_name = "similar_doctors"

urlpatterns = [
	# home page
	path('', views.index, name='index'),
	
	# view doctor
	path('doctor/<doctor_id>/', views.doctor_info, name="doctor_info"),
]