from django.urls import path
from . import views
app_name = 'Content'
urlpatterns = [
    path('Create', views.CreateBook, name='CreateBook'),
    path('Book/Book<int:ID_User>_<int:ID_Book>', views.BookView, name='Book'),
]