import markdown
import pygments
from django.shortcuts import render, get_object_or_404
from .models import Post, Category


def index(request):

    post_list = Post.objects.all().order_by('-created_time')
    return render(request,'blog/index.html', context={
        'post_list': post_list,
    })


def detail(request, pk):
    # 文章标题
    # 文章的分类
    post = get_object_or_404(Post, pk=pk)
    # post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    return render(request, 'blog/single.html', context={'post': post})


# 创建文章归档
def archives(request, year, month):

    post_list = Post.objects.filter(
        created_time__year=year,
        created_time__month=month,
    ).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})
