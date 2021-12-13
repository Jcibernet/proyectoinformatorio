from django.shortcuts import render

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

    ctx = {}

    ctx['posteo'] = post

    return render(request, 'posteos/detallePosteo.html', ctx)

def PostSobreODS(request, pk):

    categoria = Categoria.objects.get(pk = pk)

    posts = Post.objects.filter(id_categoria = categoria)

    ctx = {'posteos': posts, 'categoria': categoria}

    return render(request, 'posteos/posteosPorODS.html', ctx)