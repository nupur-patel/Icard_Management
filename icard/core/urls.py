from django.urls import path
from . import views

urlpatterns = [
	path('',views.index, name="index"),
	path('student-profile/<int:id>', views.profile, name = "profile")
]