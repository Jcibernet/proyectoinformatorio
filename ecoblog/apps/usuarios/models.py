from django.db import models

from django.contrib.auth.models import AbstractUser

class Rol(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre


class Usuario(AbstractUser, models.Model):


    rol=models.ForeignKey(Rol, on_delete=models.CASCADE, null=True)
    #def setrol(self, role):
        #self.rol=role