from django.db import models
from usuario.models import Dono
from django.utils.deconstruct import deconstructible
import time
from uuid import uuid4

STATUS_ANIMAL = (
    (1, "Perdido"),
    (2, "Comunicado"),
    (3, "Encontrado")
)

# criado para alterar o nome da imagem a ser salva
@deconstructible
class UploadToPathAndRename(object):

    def __init__(self, path):
        self.sub_path = path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # get filename
        if instance.pk:
            filename = '{}.{}'.format(instance.pk, ext)
        else:
            # set filename as random string
            filename_add = '{}'.format(uuid4().hex)
            filename_add = filename_add[0:9]
            filename = '{}.{}'.format(filename_add, ext)
        # return the whole path to the file
        return self.sub_path + filename


# Create your models here.
class Animal(models.Model):
    foto  = models.ImageField(upload_to=UploadToPathAndRename('{}'.format(time.strftime("%Y_%m_%d_"))))
    nome  = models.CharField(max_length=100)
    idade = models.CharField(max_length=3, blank=True)
    cidade_desaparecimento = models.CharField(max_length=50)
    estado_desaparecimento = models.CharField(max_length=50)
    status = models.IntegerField(choices=STATUS_ANIMAL, default=1, blank=True)
    dono = models.ForeignKey(Dono, on_delete=models.CASCADE,  null=True)
    informacoes_extras = models.TextField(max_length=250, blank=True)

    def __str__(self):
        return self.nome


class Contato(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nome
