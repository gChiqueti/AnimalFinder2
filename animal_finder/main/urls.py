from django.contrib import admin
from django.urls import path

from .views import home, cadastrar_animal
from .views import meus_animais, animal_edit
from .views import animal_delete, animal_encontrado

urlpatterns = [
    path("", home, name="home"),
    path("novo_animal/", cadastrar_animal, name="novo_animal"),
    path("meus_animais/", meus_animais, name="meus_animais"),
    path("<int:id>/edit/", animal_edit, name="animal_edit"),
    path("<int:id>/delete/", animal_delete, name="animal_delete"),
    path('<int:id>/animal_encontrado', animal_encontrado, name='animal_encontrado'),

]
