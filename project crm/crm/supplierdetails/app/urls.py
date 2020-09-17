from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
   #path('home_1',views.home_1,name="home1"),
    path('home_2',views.home_2,name="home2"),
 
]