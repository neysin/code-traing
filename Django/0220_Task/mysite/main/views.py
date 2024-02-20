from django.shortcuts import render

def index(request):
    return render(request, "main/index.html")

def about(request):
    return render(request, "main/about.html")

def notice(request):
    return render(request, "main/notice.html")

def 1(request):
    return render(request, "main/notice/1.html")

def 2(request):
    return render(request, "main/notice/2.html")

def 3(request):
    return render(request, "main/notice/3.html")

def cotact(request):
    return render(request, "main/contact.html")

def a(request):
    return render(request, "main/a.html")

def b(request):
    return render(request, "main/a/b.html")

def c(request):
    return render(request, "main/a/b/c.html")

def d(request):
    return render(request, "main/a/b/c/d.html")

def user(request):
    return render(request, "main/user.html")

def hojun(request):
    return render(request, "main/user/hojun.html")

def mini(request):
    return render(request, "main/user/mini.html")