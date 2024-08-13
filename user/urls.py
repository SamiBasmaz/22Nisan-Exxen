from django.urls import path
from .views import *




urlpatterns = [
    path('register/', UserRegister, name = 'register'),
    path('login/', userLogin, name='login'),
    path('logout/', userLogout, name='logout'),
    path('password_change/', passwordChange, name="password_change"),
    path('account_delete/', account_delete, name="account_delete"),
    
]
