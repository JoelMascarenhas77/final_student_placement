from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render, redirect
from django.urls import reverse


class LoginCheckMiddleWare(MiddlewareMixin):
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        modulename = view_func.__module__
        user = request.user


        if user.is_authenticated:
            if user.is_admin == True:
                if modulename == "app.admin_views" or modulename == "django.views.static":
                    pass
                elif modulename == "app.auth_views":
                    pass
                else:
                    return redirect("admin_home")
                
            
            elif user.is_admin == False:
                if modulename == "app.stud_views" or modulename == "django.views.static":
                    pass
                elif modulename == "app.auth_views":
                    pass
                else:
                    return redirect("stud_home")  
                
   
        
               
    
    #if request.path == reverse("login") :
    # return redirect("login")