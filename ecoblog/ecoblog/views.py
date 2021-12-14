from django.shortcuts import render


from apps.posts.models import Post

def inicio(request):


    posts = Post.objects.all().order_by('-id')

    topTres = Post.objects.all().order_by('-id')[:3]

    ctx = {}
    ctx['posteos'] = posts
    ctx['toptres'] = topTres

    return render(request, 'tech-index.html', ctx)

