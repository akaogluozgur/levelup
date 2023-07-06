from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

def index(request):
    posts = Post.objects.all().order_by("date")[:3]
    return render(request, "blog/index.html", {"posts": posts})

def posts(reqests):
    posts = Post.objects.all().order_by("date")
    return render(reqests, "blog/posts.html", {"posts": posts})

def post_detail(request, slug):
    selected_post = get_object_or_404(Post, slug=slug)
    return render(
        request,
        "blog/post-detail.html",
        {
            "post": selected_post,
            "post_tags": selected_post.game.tags.all()
        }
    )
