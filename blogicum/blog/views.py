from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from blog.models import Post, Category
from .constants import recent_num_post


def get_recent_posts():
    return Post.objects.filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now()
    )


def index(request):
    template = 'blog/index.html'
    posts = get_recent_posts().order_by('-pub_date')[:recent_num_post]
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


def post_detail(request, pk):
    template = 'blog/detail.html'
    post = get_object_or_404(
        Post,
        pk=pk,
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    )
    context = {
        'post': post,
    }
    return render(request, template, context)
