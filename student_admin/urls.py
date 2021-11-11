from django.urls import path
from student_admin.views import *


urlpatterns=[

    path('',homepage,name='homepage'),
    path('student_reg',student_reg_home,name='student_reg_home'),
    path('admin_reg',admin_reg_home,name='admin_reg_home'),
    path('std_register',std_register,name='std_register'),
    path('admin_register',admin_register,name='admin_register'),
    path('login',login,name='login'),
    path('delete_student',delete_student,name='delete_student'),
    path('go_profile',go_profile,name='go_profile'),
    path('delete_admin_session',delete_admin_session,name='delete_admin_session')

]

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
