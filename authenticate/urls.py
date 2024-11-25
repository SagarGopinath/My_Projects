from django.urls import path
from .views import UserReg
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/',UserReg.as_view(),name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]


