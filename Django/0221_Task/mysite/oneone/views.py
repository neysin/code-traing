from django.shortcuts import render
from django.http import HttpResponse

def oneone_list(request):
    return HttpResponse("oneone_list")

def oneonedetails(request, pk):
    return HttpResponse(f"Oneone Details Page: {pk}")
