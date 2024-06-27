from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from blog.models import Post, Category
from .constants import RECENT_NUM_POST


def get_recent_posts():
    return Post.objects.filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now()
    )


def index(request):
    template = 'blog/index.html'
    posts = get_recent_posts()[:RECENT_NUM_POST]
    context = {
        'post_list': posts
    }
    return render(request, template, context)


def category_posts(request, slug):
    template = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=slug,
        is_published=True,
        created_at__lte=timezone.now()
    )
    posts = get_recent_posts().filter(category=category)
    context = {
        'category': category.title,
        'post_list': posts
    }
    return render(request, template, context)


def get_filtered_posts():
    return Post.objects.filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    )


def post_detail(request, pk):
    template = 'blog/detail.html'
    filtered_posts = get_filtered_posts()
    post = get_object_or_404(filtered_posts, pk=pk)
    context = {
        'post': post,
    }
    return render(request, template, context)
