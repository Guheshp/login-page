from django.urls import path 
from . import views 


urlpatterns = [

    # -----------------------home page ------------------------------ #
    # --------------------------------------------------------------- #

    path("", views.Home, name="my-home"),

    # -----------------------Sign Up for user ----------------------- #
    # --------------------------------------------------------------- #

    path("signup", views.SignUp, name="my-signup"),

    # ----------------------- Sign In for user ---------------------- #
    # --------------------------------------------------------------- #

    path("signin", views.SignIn, name="my-signin"),

    # ----------------------- Sign Out for user --------------------- #
    # --------------------------------------------------------------- #

    path("signout", views.SignOut, name="my-signout"),
    

]

