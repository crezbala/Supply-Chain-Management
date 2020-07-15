from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .forms import CreateUserForm
from .models import designerProfile
from .forms import ProfilesForm


# Create your views here.
def log(request):
    return render(request,"designer/login.html")



def signup(request):
    usrname=request.POST.get("regusername")
    email=request.POST.get("regemail")
    password=request.POST.get("regpassword")
    confirmpassword=request.POST.get("regconpassword")
    return render(request,"designer/index.html")

# def home(request):
   
           
        
#     if request.method == 'POST':
#         username = request.POST.get('logusername')
#         password = request.POST.get('logpassword')
        
#         user1 = authenticate(request, username = username , password = password)

#         if user1 is not None:
#             login(request , user1)
#             return render(request, 'designer/index.html')
#         else:
#             messages.error(request, 'username or password is incorrect')
            


#     context = {'form':form}
#     return render(request, 'designer/login.html',context)



def registration(request):
    usrname=request.POST.get("username")
    firname=request.POST.get("firstname")
    lasname=request.POST.get("lastname")
    password=request.POST.get("password")
    confirmpassword=request.POST.get("confirmpassword")
    mail=request.POST.get("mail")
    categ=request.POST.get("category")
    brandname=request.POST.get("brandname")
    about=request.POST.get("about")
    # print("username:"usrname)
    return render(request,"designer/success.html",{'username':usrname,'category':categ,'firstname':firname,'lastname':lasname,'password':password,'confirmpassword':confirmpassword,'mail':mail,'brandname':brandname,'about':about})


def reqregister(request):
    print("inside reqregister method")
    form = CreateUserForm()
    if request.method == 'POST':  
        form = CreateUserForm(request.POST)
        print("252")  
        if form.is_valid():
            # form.save()
            user = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            print(user,email)
            # messages.info(request,'Account created try log in')
        
    context = {'form':form}
    return render(request,"designer/register.html",context)

def loginreq(request):
    print("inside loginreq")
    return render(request,"designer/login.html")

def indexreq(request):
    return render(request,"designer/index.html")

def profilereq(request):
    return render(request,"designer/profile.html")

def editprofilereq(request):
    return render(request,"designer/editprofile.html")

def samplereq(request):
    return render(request,"designer/sample.html")

def timelinereq(request):
    return render(request,"designer/timeline.html")

def logoutreq(request):
    return render(request,"designer/logout.html")

def base(request):
    return render(request,"designer/base.html")
