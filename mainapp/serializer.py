from . import models
from rest_framework  import serializers

#Serializer for User Table
class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.User
		exclude=["last_login" ,"date_joined" , "groups" , "user_permissions"]

#Serializer for Course Table
class CourseSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Course
		fields = "__all__"

#Serializer for Subject Table
class SubjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Subject
		fields = "__all__"

#Serializer for Billing Table
class BillingSerializer(serializers.ModelSerializer):
	class Meta :
		model = models.Billing
		fields = "__all__"