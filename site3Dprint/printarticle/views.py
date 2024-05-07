from django.shortcuts import render
from .models import Post
from django.http import Http404


def post_detail(request, id):
    try:
        post = Post.published.get(id=id)
    except Post.DoesNotExist:
        raise Http404('No Post found')
    return render(request, 'printarticle/post/detail.html', {'post': post})


def post_list(request):
    posts = Post.published.all()
    return render(request, 'printarticle/post/list.html', {'post': posts})
