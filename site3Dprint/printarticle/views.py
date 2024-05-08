from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import Http404


def post_list(request):
    posts = Post.published.all()
    return render(request, 'printarticle/post/list.html', {'posts': posts})


def post_detail(request, year, mont, day, post):
    post = get_object_or_404(Post,
                             status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__year=year,
                             publish__mont=mont,
                             publish__day=day)
    return render(request, 'printarticke/post/detail.html')
