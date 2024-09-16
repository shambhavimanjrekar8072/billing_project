from django.urls import path
from . import views

urlpatterns = [

	#for users
	path('users' , views.UserListView.as_view()),
	path('login_user' , views.LoginUserView.as_view()),
	path('user/<str:pk>' , views.UserDetailView.as_view()),
	path('inactiveuser' , views.GetInActiveUser.as_view()),
	path('forgetpassword' , views.ForgetPasswordView.as_view()),
	
	#for courses
	path('courses' , views.CourseListView.as_view()),
	path('course/<str:pk>' , views.CourseDetailView.as_view()),

	#for subject
	path('subjects' , views.SubjectListView.as_view()),
	path('subject/<str:pk>' , views.SubjectDetailView.as_view()),

]