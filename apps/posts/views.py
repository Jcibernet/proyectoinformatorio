from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render

from django.views.generic import CreateView
from django.urls import reverse_lazy

from apps.usuarios.models import Usuario
from .forms import Formulario_nuevo_post


import random

from .models import Comentario, Post, Categoria

# Create your views here.
def ListarPosteos(request):

    posteos = Post.objects.all()

    #CONTEXTO
    ctx = {}
    ctx['posteos'] = posteos
    
    return render(request, 'posteos/listarPosteos.html', ctx)


def ComentarPost(request, pk, user):

    user = Usuario.objects.get(pk = user)

    post = Post.objects.get(pk = pk)

    comment = Comentario()
    comment.setUsuario(user)
    comment.setCuerpo(request.POST.get('comentario'))
    comment.setPost(post)
    comment.save()

    return redirect('posts:detalle_post', pk = pk)

def DetallePost(request, pk):

    post = Post.objects.get(pk = pk)

    comentarios = Comentario.objects.filter(post = pk)

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
    ctx['comentarios'] = comentarios
    ctx['url'] = request
    # ctx['url'] = f"https://web.whatsapp.com/send?text=http%3A%2F%2F{request.get_host}%2Fposteos%2F{post.pk}"

    return render(request, 'posteos/detallePosteo.html', ctx)

def PostSobreODS(request, pk):

    categoria = Categoria.objects.get(pk = pk)

    posts = Post.objects.filter(id_categoria = categoria)

    ctx = {'posteos': posts, 'categoria': categoria}

    return render(request, 'posteos/posteosPorODS.html', ctx)


    # return render(request, 'posteos/detallePosteo.html')
    

    # comentario = request.POST.get('comentario')

    # print(type(comentario))

    # comment = Comentario.objects.create()
    # print()

 
        

class NuevoPost(CreateView):

    model = 'Post'
    template_name = 'posteos/nuevoPost.html'
    form_class = Formulario_nuevo_post
    success_url = reverse_lazy('inicio')