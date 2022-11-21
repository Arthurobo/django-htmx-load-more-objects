from django.shortcuts import render
from .models import Post
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def home(request):
    posts = _load_posts(request)
    context = {"posts": posts,}
    return render(request, "posts/all-posts.html", context)


def list_load_posts_view(request):
    posts = _load_posts(request)
    context = {"posts": posts,}
    return render(request, "posts/partials/all-posts.html", context)


def _load_posts(request):
    page = request.GET.get("page")
    posts = Post.objects.all().order_by('-date_created')
    paginator = Paginator(posts, 3)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return posts