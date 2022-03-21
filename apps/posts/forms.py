from django import forms

from .models import Post

class Formulario_nuevo_post(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'
        #fields = ['nombre', 'descripcion']