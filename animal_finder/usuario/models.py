from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.signals import post_delete
from django.dispatch import receiver

class DonoManager(BaseUserManager):
    def create_user(self, email, nome, telefone, password=None):
        if not email: raise ValueError("Usuário precisa ter um email")
        if not nome: raise ValueError("Usuário precisa ter um nome")
        if not telefone: raise ValueError("Usuário precisa ter um telefone")
        user = self.model(email = self.normalize_email(email),
                          nome=nome,
                          telefone=telefone,)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, nome, telefone, password):
        user=self.create_user(email=self.normalize_email(email),
                              nome=nome,
                              password=password,
                              telefone=telefone)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Dono(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", unique=True, max_length=100)
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)

    date_joined = models.DateTimeField(verbose_name="date_joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last_login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome', 'telefone']

    objects = DonoManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
