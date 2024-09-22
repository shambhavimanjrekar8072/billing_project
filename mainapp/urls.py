from django.urls import path
from . import views

urlpatterns = [

	#for users

	path('users' , views.UserListView.as_view()),  #for list of users and creating user
	path('login_user' , views.LoginUserView.as_view()), #for logging in the user
	path('user/<str:username>' , views.UserDetailView.as_view()), #for getting detail of specific user , delete and update the user
	path('inactiveuser' , views.GetInActiveUser.as_view()), #getting the list of inactive user
	path('forgetpassword' , views.ForgetPasswordView.as_view()), #for forgetting the password
	path('logout' , views.LogOutAPI.as_view()),

	
	#for courses

	path('courses' , views.CourseListView.as_view()), #for getting the list of courses and creating the course
	path('course/<str:pk>' , views.CourseDetailView.as_view()), # for getting the detail for specific course and deleting , updating the course

	#for subject
	
	path('subjects' , views.SubjectListView.as_view()), #for getting the list of subject and creating the subject
	path('subject/<str:pk>' , views.SubjectDetailView.as_view()), # for getting the detail for specific subject and deleting , updating the subject

]