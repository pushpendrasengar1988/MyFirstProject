from django.http import HttpResponse , HttpResponseRedirect , HttpResponseNotFound
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from .models import UserProfile
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
import datetime
from . import forms
from django.contrib import messages

def index(request):
    return HttpResponse("Hello, world. You're at the kiwi index1.")

def dashboard(request):
    userProfile = UserProfile.objects.get(user_id=request.user.id)

    return render(request, 'dashboard.html',
                  {
                      'userProfile': userProfile
                  }
                  )

def getLogin(request):
    return render(request, 'login.html')

def userLogout(request):
    userProfile = UserProfile.objects.get(user_id=request.user.id)
    userProfile.last_logout=datetime.datetime.now()
    userProfile.save()
    logout(request)
    return HttpResponseRedirect(reverse('getLogin'))



def getRegister(request):
    return render(request, 'register.html')

def getuserupdate(request):
    userProfile=UserProfile.objects.get(user_id=request.user.id)
    fs = FileSystemStorage()
    uploaded_file_url = fs.url(userProfile.photo)
    return render(request, 'update-user.html',
                  {
                      'userProfile': userProfile,
                      'uploaded_file_url':uploaded_file_url
                  }
    )

def postuserupdate(request):
    if request.method == 'POST':

                fs = FileSystemStorage()
                firstname = request.POST['firstname']
                lastname = request.POST['lastname']
                phone = request.POST['phone']
                email = request.POST['email']
                username = request.POST['username']
                if request.POST.get("profilepic") != '':
                    myfile = request.FILES['profilepic']

                    filename = fs.save(myfile.name, myfile)


                user = User.objects.get(id=request.user.id)
                user.first_name = firstname
                user.last_name = lastname
                user.email = email
                user.username = username
                user.save()

                userProfile = UserProfile.objects.get(user_id=request.user.id)
                userProfile.phone=phone
                if request.POST.get("profilepic") != '':
                    userProfile.photo = filename
                userProfile.save()
                messages.success(request, 'User Profile has been updated')
                return render(request, 'update-user.html',
                                         {
                            'userProfile': userProfile,
                            'uploaded_file_url':  fs.url(userProfile.photo)
                            }
                )

    else:
        return HttpResponseRedirect(reverse('getuserupdate'))

def postLogin(request):
    args = {}
    if request.method == 'POST':

            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user:
                   login(request, user)
                   userProfile = UserProfile.objects.get(user_id=request.user.id)
                   userProfile.login_count +=1
                   userProfile.save()
                   return HttpResponseRedirect(reverse('dashboard'))

            else:
                messages.error(request,'invalid login credentials')
                return render(request, 'login.html')
    else:
      return HttpResponseRedirect(reverse('getLogin'))

def postRegister(request):
    if request.method =='POST' and request.FILES['profilepic']:
       form = forms.UserSignUpForm(data=request.POST)
       if form.is_valid():

               firstname = request.POST['firstname']
               lastname = request.POST['lastname']
               phone = request.POST['phone']
               email = request.POST['email']
               psw = request.POST['password']
               username=request.POST['username']

               myfile = request.FILES['profilepic']
               fs = FileSystemStorage()
               filename = fs.save(myfile.name, myfile)


               user = User.objects.create_user(first_name=firstname, last_name=lastname,email=email,password=psw,username=username)

               UserProfile.objects.get_or_create(user_id=user.id ,phone=phone,photo=filename)
               return redirect('/kiwi/login')
       else:
          return render(request, 'register.html',{'form':form} )

    else:
        return HttpResponseRedirect(reverse('getRegister'))



