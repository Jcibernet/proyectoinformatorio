from django.shortcuts import render


from apps.posts.models import Categoria, Comentario, Post

def inicio(request):

    posts = Post.objects.all().order_by('-id')

    topTres = Post.objects.all().order_by('-id')[:3]

    ods = Categoria.objects.all().order_by('id')

    comentarios = Comentario.objects.all()


    
    ctx = {}
    ctx['posteos'] = posts
    ctx['toptres'] = topTres
    ctx['allOds'] = ods
    ctx['comentarios'] = comentarios
    
    return render(request, 'tech-index.html', ctx)

