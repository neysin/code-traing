from django.shortcuts import render
from django.http import HttpResponse

def free_list(request):
    return HttpResponse("free_list")

def freedetails(request, pk):
    return HttpResponse(f"Free Details Page: {pk}")

