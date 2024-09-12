from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework.views import APIView 
from rest_framework import status
from . import models ,serializer
from django.http import HttpResponse
from django.contrib import auth  
from django.db.models import Q
from django.conf import settings

# Create your views here.

# class LogInView(APIView):
# 	def get(self , request , )


class UserListView(APIView):
	def get(self , request):
		users = models.User.objects.all()
		ser = serializer.UserSerializer(users , many=True)
		return Response(ser.data)