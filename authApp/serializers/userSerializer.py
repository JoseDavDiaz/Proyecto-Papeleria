from rest_framework import serializers
from authApp.models.user import User

class userSerializer (serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id','username','password','name','email']