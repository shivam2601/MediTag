from django.contrib import admin
from django.urls import path
from . import views
app_name = "basic_qr"
urlpatterns = [
path('',views.landing,name="landing"),
path('medform/',views.medform,name="medform"),
path('update-medform/<str:pk>',views.updateMedform,name="update-medform"),
path('update-doc/<str:pk>',views.updateDocument,name="update-document"),
path('profile/<str:pk>',views.profile,name="profile"),
path('login/',views.loginPage,name="login"),
path('logout/',views.logoutUser,name="logout"),
path('register/',views.registerPage,name="register"),
path('faq/',views.registerPage,name="faq"),
path('view-docs/<str:pk>',views.displayDocuments,name="display-documents"),
path('upload-doc/',views.uploadDocument,name="upload-document"),
path('delete-doc/<str:pk>',views.deleteDocument,name="delete-document"),

]
