from . import models
from rest_framework  import serializers

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.User
		exclude=["last_login" ,"date_joined" , "groups" , "user_permissions"]

class CouserSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Course
		fields = "__all__"

class SubjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Subject
		fields = "__all__"

class BillingSerializer(serializers.ModelSerializer):
	class Meta :
		model = models.Billing
		fields = "__all__"