from django.contrib import admin
from .models import * 
# Register your models here.

class UserAdditionalInfoAdmin(admin.ModelAdmin):
    list_display = ['username',"first_name","last_name",'city','contact_no','address','email']

admin.site.register(UserAdditionalInfo, UserAdditionalInfoAdmin)


class AccountmanagerAdmin(admin.ModelAdmin):
    list_display = ['name']
    def user(self,obj):
        name = obj.name
        user = Accountmanager.objects.get(id=name)
        return user

admin.site.register(Accountmanager, AccountmanagerAdmin)




class UsermanagerAdmin(admin.ModelAdmin):
    list_display = ['user','manager_name','user_contact_no','user_email']
    def user(self,obj):
        manager_name_id = obj.manager_name_id
        user = Usermanager.objects.get(id=manager_name_id)
        return user

admin.site.register(Usermanager, UsermanagerAdmin)






