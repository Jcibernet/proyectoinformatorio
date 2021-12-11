from django.db import models

#Modelo de Categoria
class Categoria(models.Model):

    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

# Modelo de POST
class Post(models.Model):

    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255)
    cuerpo = models.TextField()
    fechaCreacion = models.DateField(auto_now_add=True)
    imagen = models.ImageField(upload_to='imagenes_posts', null=True)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

