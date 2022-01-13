from django.shortcuts import render
from.models import *
from.serializer import * 
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.mail import send_mail as send_email
class Signup(APIView):
    def post(self, request):
        data=request.data
        first_name = data['first_name']
        last_name = data['last_name']
        username = data['username']
        city = data['city']
        contact_no = data['contact_no']
        address = data['address']
        email = data['email']
       
        if User.objects.filter(username=username).exists():
            return Response({
                'status': 0,
                'message': 'user already exist.'
                })
        else:
            user = User.objects.create(username=username,email=email)
            if user:
                user.save()
                user1 = UserAdditionalInfo.objects.create(username_id=user.id,first_name=first_name,last_name=last_name,city=city,contact_no=contact_no,email=email,address=address)
                user1.save()

                user_count = User.objects.all().count()
              
                if user_count == 2:
                    manager = Accountmanager.objects.get(id=1)
                    manage_id = manager.id 
                    z = Usermanager.objects.create(user_id=user.id,manager_name_id=manage_id,user_contact_no=contact_no,user_email=email)
                    
                else:
                    c = Usermanager.objects.latest('id')
                    print(c)
                    manage_id = c.manager_name_id
                    
                    print(manage_id)
                    if manage_id == 25:
                        manage_id = 1
                    else:
                        manage_id = manage_id + 1
                        print(manage_id)
                    user_relation = Usermanager.objects.create(user_id=user.id,manager_name_id=manage_id,user_contact_no=contact_no,user_email=email)
                
                account_manager  = Accountmanager.objects.get(id=manage_id)
                response = send_email(
                        subject = "important message",
                        message = 'you are assign account manager' + account_manager.name + 'you can meet soon ',
                        from_email = 'webnetbelgium@gmail.com',
                        recipient_list = [email],
                        fail_silently=False,
            )
                return Response({
                    'status': 1,
                    'message': 'successfully'
                    })

