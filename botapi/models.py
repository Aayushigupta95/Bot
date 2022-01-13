from django.db import models
from django.contrib.auth.models import User

class UserAdditionalInfo(models.Model):

    username = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True)
    city = models.CharField(max_length=100, null=True,blank=True)
    contact_no = models.CharField(max_length=12)
    address = models.CharField(max_length=100, null=True,blank=True)
    email = models.CharField(max_length=100, null=True)
    def __str__(self):
        return str(self.username_id)

class Accountmanager(models.Model):
    name = models.CharField(max_length=100, null=True,blank=True)
    
    def __str__(self):
        return self.name



class Usermanager(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    manager_name = models.ForeignKey(Accountmanager, on_delete=models.CASCADE,null=True)
    user_contact_no = models.CharField(max_length=12)
    user_email = models.EmailField(max_length=40, null=True)
    def __int__(self):
        return self.id




   