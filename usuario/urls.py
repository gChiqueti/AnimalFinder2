from django.contrib import admin
from django.urls import path
from .views import register
from .views import user_login
from .views import user_logout

urlpatterns = [
    path("novo", register, name="register"),
    path("login", user_login, name="login"),
    path("logout", user_logout, name="logout"),
]
