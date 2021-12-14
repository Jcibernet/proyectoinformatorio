from django.shortcuts import render

from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import Formulario_nuevo_post

import random

from .models import Post, Categoria

# Create your views here.
def ListarPosteos(request):

    posteos = Post.objects.all()

    #CONTEXTO
    ctx = {}
    ctx['posteos'] = posteos
    
    return render(request, 'posteos/listarPosteos.html', ctx)

def DetallePost(request, pk):

    post = Post.objects.get(pk = pk)

    items = list(Post.objects.filter(id_categoria = post.id_categoria))

    ods = Categoria.objects.all().order_by('id')

    if len(items) == 1:
        topTres = random.sample(items, 1)
    elif len(items) == 2:
        topTres = random.sample(items, 2)
    elif len(items) > 2:
        topTres = random.sample(items, 3)


    ctx = {}

    ctx['posteo'] = post
    ctx['masPosts'] = topTres
    ctx['allOds'] = ods

    return render(request, 'posteos/detallePosteo.html', ctx)

def PostSobreODS(request, pk):

    categoria = Categoria.objects.get(pk = pk)

    posts = Post.objects.filter(id_categoria = categoria)

    ctx = {'posteos': posts, 'categoria': categoria}

    return render(request, 'posteos/posteosPorODS.html', ctx)


class NuevoPost(CreateView):

    model = 'Post'
    template_name = 'posteos/nuevoPost.html'
    form_class = Formulario_nuevo_post
    success_url = reverse_lazy('posts:listar_posteos')