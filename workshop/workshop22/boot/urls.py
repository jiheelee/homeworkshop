from django.urls import path
from . import views

app_name = "boot"

urlpatterns = [
    path("test/", views.test, name="test"),
    
    
]