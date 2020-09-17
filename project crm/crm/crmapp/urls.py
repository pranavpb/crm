from django.urls import path
from . import views

urlpatterns = [
    #path('',views.home,name="home"),
    path('',views.details,name="details"),
    path('salary/',views.salary,name="salary"),
    #path('role/',views.role,name="role"),
]