from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework.views import APIView 
from rest_framework import status
from . import models ,serializer
from django.http import HttpResponse
from django.contrib import auth  
from django.db.models import Q
from django.conf import settings
from rest_framework import generics


class UserListView(APIView):
	def get(self , request):
		users = models.User.objects.all()
		ser = serializer.UserSerializer(users , many=True)
		return Response(ser.data , status=status.HTTP_200_OK)
	def post(self , request):
		ser = serializer.UserSerializer(data =  request.data)
		if ser.is_valid():
			ser.save()
			demo = models.User.objects.get(username=request.data["username"])
			demo.set_password(request.data["password"])
			demo.save()
			return Response(ser.data , status.HTTP_201_CREATED)
		else :
			return Response(ser.errors , status.HTTP_400_BAD_REQUEST)

class LoginUserView(APIView):
	def get(self , request ):
		user = auth.authenticate(username = request.data["username"] , password=request.data["password"])
		if user is not None :
			ser =  serializer.UserSerializer(user)
			auth.login(request , user)
			return Response(ser.data , status.HTTP_202_ACCEPTED)
		else:
			return Response(status=status.HTTP_400_BAD_REQUEST)
		
class ForgetPasswordView(APIView):
	def get(self , request):
		user = request.user
		if user.check_password(request.data["old_password"]):
			user.set_password(request.data["new_password"])
			user.save()
			return Response(status=status.HTTP_204_NO_CONTENT)
		else :
			return Response(status=status.HTTP_401_UNAUTHORIZED)
		

class UserDetailView(APIView):

	def getUser(self , pk):
		try:
			return models.User.objects.get(pk = pk)
		except:
			return None

	def get(self , request , pk):
		user = self.getUser(pk)
		if user is None:
			return Response(status=status.HTTP_404_NOT_FOUND)
		ser = serializer.UserSerializer(user)
		return Response(ser.data , status.HTTP_200_OK)
	
	def patch(self , request , pk):
		user = self.getUser(pk)
		ser = serializer.UserSerializer(user , data=request.data , partial=True)
		if ser.is_valid():
			ser.save()
			return Response(ser.data , status = status.HTTP_202_ACCEPTED)
		return Response(ser.errors , status = status.HTTP_400_BAD_REQUEST)

	def delete(self , request , pk):
		user = self.getUser(pk)
		if user is None:
			return Response(status=status.HTTP_404_NOT_FOUND)
		user.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
	
class GetInActiveUser(APIView):
	def get(self , request):
		users = models.User.objects.filter(is_active = False)
		ser = serializer.UserSerializer(users , many = True)
		return Response(ser.data , status.HTTP_200_OK)
	
class CourseListView(generics.ListCreateAPIView):
	queryset=models.Course.objects.all()
	serializer_class = serializer.CourseSerializer

class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = models.Course.objects.all()
	serializer_class = serializer.CourseSerializer

class SubjectListView(generics.ListCreateAPIView):
	queryset=models.Subject.objects.all()
	serializer_class = serializer.SubjectSerializer

class SubjectDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = models.Subject.objects.all()
	serializer_class = serializer.SubjectSerializer

