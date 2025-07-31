from django.contrib import admin
from django.urls import path,include
from book_app import views

urlpatterns = [
   path('',views.homebook,name="home"), 
   path('addbook/',views.addbooks,name="addbook"),
   path('viewbook/<int:pk>/',views.viewbooks,name="viewbook"),
   path('updatebook/<int:pk>/',views.updatebook,name="updatebook"),
   path('deletebook/<int:pk>/',views.deletebook,name="deletebook"),
   path('booklist/',views.book_list,name="booklist"),  
]   