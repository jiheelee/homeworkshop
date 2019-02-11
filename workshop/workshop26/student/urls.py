from django.urls import path
from . import views

app_name = "student"

urlpatterns= [
    path('',views.list,name="list"),
    path('create/',views.create, name="create"),
    ]