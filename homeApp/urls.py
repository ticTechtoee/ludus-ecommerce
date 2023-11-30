from django.urls import path
from . import views

app_name = 'homeApp'

urlpatterns = [
    path('', views.ViewIndexPage, name="IndexPageView"),
    path('items_list_page/', views.ViewShopSideVersion, name="ShopSideVersionView"),
]
