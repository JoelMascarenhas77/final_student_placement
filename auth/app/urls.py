from django.urls import path
from . import auth_views
from . import stud_views
from . import admin_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", auth_views.user_login, name="login"),
    path("logout/", auth_views.user_logout, name="logout_user"),
    path("reset/", auth_views.reset_password, name="password_reset"),
    path("admin_home/", admin_views.home, name="admin_home"),
    path("admin/add_student/", admin_views.add_student, name="add_student"),
    path("admin/manage_student/", admin_views.manage_student, name="manage_student"),
    path('delete_student/<int:student_pid>/', admin_views.delete_student, name='delete_student'),
    path("admin/manage_comapny/", admin_views.manage_company, name="manage_company"),
    path("admin/manage_course/", admin_views.manage_course, name="manage_course"),
    path("admin/prediction/", admin_views.update_prediction, name="prediction"),
    path("admin/add_student_file/", admin_views.add_student_file, name="add_student_file"), 
    path("admin/feedback/", admin_views.feedback, name="admin_feedback"),
    path('add_company_file/', admin_views.add_company_file, name='add_company_file'),
    path('add_course_file/', admin_views.add_course_file, name='add_course_file'),
    path("student_home/", stud_views.home, name="student_home"),
    path("student/prediction/", stud_views.prediction, name="student_prediction"),
    path("student/feedback/", stud_views.feedback, name="student_feedback"),
    path("student/add_certificates/", stud_views.add_certificates_and_reports, name="add_certificates"),
    path("student/manage_courses/", stud_views.manage_courses, name="manage_courses"),
    path("student/apply_course/", stud_views.apply_course, name="apply_course"),
    path("student/update_profile_picture/", stud_views.update_profile_picture, name="update_profile_picture"),
    path('add_placement_file/', admin_views.add_placement_file, name='add_placement_file'),
    path('manage_placement/', admin_views.manage_placement, name='manage_placement'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
