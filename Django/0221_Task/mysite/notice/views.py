from django.shortcuts import render
from django.http import HttpResponse

def notice_list(request):
    return HttpResponse("notice_list")

def free(request):
    return HttpResponse("free")

def oneone(request):
    return HttpResponse("oneone")