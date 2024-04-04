from django.urls import path, include
from . import views
#from django.contrib.auth import views as auth_views



urlpatterns = [

# Shared URL's
 #path('', views.login_form, name='home'),
 path('', views.login_user, name='home'),
#path('signup/',views.signup_form, name='signup'),
path('teacher/',views.teacherdash,name='teacher'),
path('register/',views.user_register,name='register'),
path('admindash/',views.admin_dash,name='admindash'),
path('staff/',views.staff,name='staff'),
path('userview/',views.adminView,name='userview'),
path('detail/',views.detail,name='detail'),
path('salaryup/',views.admin_teacher_salary_view,name='updatesalalary')

]
