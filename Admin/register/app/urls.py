from django.urls import path
from . import views

urlpatterns = [
    path('',views.indexpage,name='index'),
    path('registerpage',views.Userregister,name='register'),
    path('loginpage',views.Loginpage,name='login'),
    path('loginuser',views.Loginuser,name='loginuser'),
    path('home',views.Home,name='home'),
    path('logout',views.Logout,name='logout'),
]