from django.shortcuts import render, redirect

from django.http import HttpResponse

from django.contrib.auth.models import User

from django.contrib import messages

from django.contrib.auth import authenticate, login, logout


# Create your views here.

 # - Home. 

def Home(request):

    return render(request, "index.html")
 # - signup. 

def SignUp(request):

    if request.method == "POST":

        #username = request.POST.get("username")
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['password']

        myuser = User.objects.create_user(username, email, password1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()
    
        messages.success(request," ur registred successfully!")

        return redirect('my-signin')

    return render(request, "signup.html")

 # - signin. 
def SignIn(request):
    
    if request.method == "POST":

        username = request.POST['username']
        password1 = request.POST['password']

        user = authenticate(username=username, password=password1)

        if user is not None:
        
            login(request, user)
            return redirect('my-home')
        
        else:

            messages.error("bad creditionals")
            return redirect("my-SignIn")

    return render(request, "signin.html")

 # - signout. 

def SignOut(request):
   logout(request)
   messages.success(request, "successfully logout")
   return redirect('my-home')



