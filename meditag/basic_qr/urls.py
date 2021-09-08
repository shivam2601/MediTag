from django.contrib import admin
from django.urls import path
from . import views
app_name = "basic_qr"
urlpatterns = [
path('',views.landing,name="landing"),
path('medform/',views.medform,name="medform"),
path('update-medform/<str:pk>',views.updateMedform,name="update-medform"),

path('profile/<str:pk>',views.profile,name="profile"),
path('login/',views.loginPage,name="login"),
path('logout/',views.logoutUser,name="logout"),
path('register/',views.registerPage,name="register"),

]
