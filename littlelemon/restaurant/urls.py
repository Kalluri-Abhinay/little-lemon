from django.contrib import admin
from django.urls import path,include
from . import views

from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [

            path("",views.index,name="home"),
            path('menu/', views.MenuItemsView.as_view(),name='menu-list'),
            path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
            path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
           
]