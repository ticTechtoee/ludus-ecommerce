from django.urls import path
from . import views

urlpatterns = [
    path('', views.ViewSignUpPage, name="SignUpPageView"),
]
