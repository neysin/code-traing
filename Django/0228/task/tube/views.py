from django.shortcuts import render
from .models import Post


def tube_list(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "tube/tube_list.html", context)

def tube_detail(request):
    pass

def tube_create(request):
    pass

def tube_update(request):
    pass

def tube_delete(request):
    pass