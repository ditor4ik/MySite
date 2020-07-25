from django.urls import path
from . import views
app_name = 'Account'
urlpatterns = [
    path('CheckIn', views.CheckInForm, name='CheckInForm'),
    path('SignIn/', views.SignInForm, name='SignInForm'),
    path('Logout/', views.Logout, name='Logout'),
    path('Profile/<int:UserId>/', views.Profile, name='Profile'),
]