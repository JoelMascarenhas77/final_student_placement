from django.urls import path
from . import auth_views 
from . import stud_views 
from . import admin_views 
from django.conf.urls.static import static
from django.conf import settings




urlpatterns = [
    path("", auth_views.user_login, name ="login"),
    path("logout/", auth_views.user_logout, name="logout_user"),
    path("reset" , auth_views.reset_password ,name = "password_reset"),


    path("admin_home/" , admin_views.home ,name = "admin_home"),
    path("admin/add_student/" , admin_views.add_student ,name = "add_student"),   
    path("admin/manage_student/" , admin_views.manage_student ,name = "manage_student"),
     
    path("student_home/" , stud_views.home , name = "student_home"),


    

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)