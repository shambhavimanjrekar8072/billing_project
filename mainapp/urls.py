from django.urls import path
from . import views

urlpatterns = [

	#for users
	path('users' , views.UserListView.as_view()),
	path('login_user' , views.LoginUserView.as_view()),
	path('user/<str:id>' , views.UserDetailView.as_view()),
	path('inactiveuser' , views.GetInActiveUser.as_view()),
	
	#courses
	path('courses' , views.CourseListView.as_view())

]