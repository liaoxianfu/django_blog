from django.shortcuts import render, get_object_or_404
from .models import Post


def index(request):

    post_list = Post.objects.all().order_by('-created_time')
    return render(request,'blog/index.html', context={
        'post_list': post_list,
    })


def detail(request, pk):
    # 文章标题
    # 文章的分类
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/single.html', context={'post': post})
