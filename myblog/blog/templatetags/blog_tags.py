from ..models import Post,Category
from django import template

register = template.Library()


# 获取最新文章
@register.simple_tag
def get_recent_post(num=5):
    return Post.objects.all().order_by('-created_time')[:num]


# 获取最新的文章归档
@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')


# 获取全部的标签
@register.simple_tag
def get_categories():
    return Category.objects.all()
