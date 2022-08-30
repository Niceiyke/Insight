from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView

from .views import RegistrationView

urlpatterns = [
    path('login',LoginView.as_view(),name='login'),
    path('login',LogoutView.as_view(),name='logout'),
     path('register',RegistrationView,name='register')
]
