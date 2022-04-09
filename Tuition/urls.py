"""Tuition URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path





from app.views import student_information,showdata,guardian_information,Gshowdata,Register,Login,home,Logout,Notice,upload,Contact_me

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',student_information,name='contact'),
   
    path('',home,name='home'),
    path('contact/',Contact_me,name='contact'),
    path('Notice/',Notice,name='notice'),
    path("upload",upload, name="upload"),
    path('data/',showdata,name='showdata'),
    path('guardian/',guardian_information,name='Information'),
    path('guardian_info/',Gshowdata,name='Information'),
    path('register/',Register, name="register"),
    path("login/",Login, name="login"),
    path("logout/",Logout, name="logout"),
]
