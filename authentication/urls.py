from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path('login', views.loginUser, name='login'),
    path('logout', views.logoutUser, name='logout'),
]