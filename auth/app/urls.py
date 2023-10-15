from django.urls import path
from . import auth_views
from . import stud_views
from . import admin_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", auth_views.user_login, name="login"),
    path("logout/", auth_views.user_logout, name="logout_user"),
    path("reset/", auth_views.reset_password, name="reset"),
    path("admin_home/", admin_views.home, name="admin_home"),
    path("admin/add_student/", admin_views.add_student, name="add_student"),
    path("admin/manage_student/", admin_views.manage_student, name="manage_student"),
    path('delete_student/<int:student_pid>/', admin_views.delete_student, name='delete_student'),
    #path("admin/manage_comapny/", admin_views.manage_company, name="manage_company"),
    path("admin/prediction/", admin_views.prediction, name="prediction"),
    path("admin/add_student_file/", admin_views.add_student_file, name="add_student_file"), 

    path("student_home/", stud_views.home, name="student_home"),
    path("student/prediction/", stud_views.prediction, name="student_prediction")

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
