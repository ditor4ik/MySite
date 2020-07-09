from django.urls import path
from . import views
app_name = 'CheckIn'
urlpatterns = [
    path('', views.CheckInForm, name='CheckInForm'),
]