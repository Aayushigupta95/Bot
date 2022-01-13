from rest_framework import serializers
from.models import * 


class UserAdditionalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAdditionalInfo
        fields = ['username',"first_name","last_name",'city','contact_no','address','email']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']


class AccountmanagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accountmanager
        fields =['name']

class UsermanagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usermanager
        fields = ['user','manager_name','user_contact_no','user_email']







