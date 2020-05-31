from django.shortcuts import render
from basic_app.forms import UserForm, UserprofileForm

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'basic_app/index.html')


@login_required
def usr_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('matcher:index'))

@login_required
def special(request):
    return HttpResponse("You are Logged In")

def register(request):

    registerd = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form =  UserprofileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()

            registerd = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserprofileForm()


    return  render(request,'basic_app/register.html',
            context={'user_form':user_form,'profile_form':profile_form,'registerd':registerd})


def  usr_login(request):
    if request.method == 'POST':
        uid = request.POST.get('inputuid')
        pswd = request.POST.get('inputPassword')
        user = authenticate(username=uid,password=pswd)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('matcher:index'))
            else:
                return HttpResponse("Account  Not Active")

        else:
            print("Someone failed to login \n ")
            print("Username: {} and Password: {}".format(uid,pswd))
            return HttpResponse("Invalid Login Request")
    else:
        return render(request,'basic_app/usr_login.html')
