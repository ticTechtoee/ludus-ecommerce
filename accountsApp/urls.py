from django.urls import path
from . import views

app_name = 'accountsApp'

urlpatterns = [
    path('signup/', views.ViewSignUpPage, name="SignUpPageView"),
    path('login/', views.ViewLoginPage, name="LogInPageView"),
]
