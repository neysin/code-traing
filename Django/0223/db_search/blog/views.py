from django.shortcuts import render
from .models import Post


def blog_list(request):
    db = Post.objects.all()
    context = {
        "db": db,
    }
    return render(request, "blog/blog_list.html", context)


def blog_detail(request, pk):
    db = Post.objects.get(pk=pk)
    context = {
        "db": db,
    }
    return render(request, "blog/blog_detail.html", context)