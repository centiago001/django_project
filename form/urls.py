from django.contrib import admin
from django.urls import path
from form import views


urlpatterns = [
    path('admin-panal/', admin.site.urls,name='ma'),
    path('',views.form),
    path('pan/',views.login_page,name='ad'),
    path('login/',views.admin_login),
    path('f_submits/',views.f_submits),
    path('delete/',views.delete_data),
    path('logout/',views.admin_logout),


]