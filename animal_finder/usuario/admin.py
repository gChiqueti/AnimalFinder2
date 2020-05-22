from django.contrib import admin
from .models import Dono

@admin.register(Dono)
class UserAdmin(admin.ModelAdmin):
    pass
