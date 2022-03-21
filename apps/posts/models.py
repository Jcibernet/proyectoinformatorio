from django.db import models

from apps.usuarios.models import Usuario

#Modelo de Categoria
class Categoria(models.Model):

    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(null=True)
    imagen = models.ImageField(upload_to='imagenes_ods', null=True)

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

class Comentario(models.Model):

    cuerpo = models.TextField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    fechaCreacion = models.DateTimeField(auto_now_add=True, null=True)

    def setCuerpo(self, cuerpo):
        self.cuerpo = cuerpo
    
    def setUsuario(self, usuario):
        self.usuario = usuario

    def setPost(self, post):
        self.post = post

    def __str__(self):
        return self.post.titulo