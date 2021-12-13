from django.shortcuts import render

from apps.posts.models import Post

def inicio(request):


    posts = Post.objects.all().order_by('-id')

    ctx = {}
    ctx['posteos'] = posts

    return render(request, 'tech-index.html', ctx)

