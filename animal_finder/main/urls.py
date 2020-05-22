from django.contrib import admin
from django.urls import path
from .views import home, cadastrar_animal

urlpatterns = [
    path("", home, name="home"),
    path("novo_animal", cadastrar_animal, name="novo_animal")
]
