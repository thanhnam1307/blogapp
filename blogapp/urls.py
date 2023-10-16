from django.urls import path
from . import views
from blogapp import views

urlpatterns = [
     path('' ,views.HomePage , name="home")
]
