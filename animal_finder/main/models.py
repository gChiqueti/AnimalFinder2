from django.db import models
from usuario.models import Dono

STATUS_ANIMAL = (
    (1, "Perdido"),
    (2, "Comunicado"),
    (3, "Encontrado")
)

# Create your models here.
class Animal(models.Model):
    foto  = models.ImageField()
    nome  = models.CharField(max_length=100)
    idade = models.CharField(max_length=3, blank=True)
    cidade_desaparecimento = models.CharField(max_length=50)
    estado_desaparecimento = models.CharField(max_length=50)
    status = models.IntegerField(choices=STATUS_ANIMAL, default=1, blank=True)
    dono = models.ForeignKey(Dono, on_delete=models.CASCADE,  null=True)
    informacoes_extras = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.nome
