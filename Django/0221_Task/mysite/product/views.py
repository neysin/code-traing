from django.shortcuts import render
from django.http import HttpResponse

def product_list(request):
    return HttpResponse("product_list")

def productdetails(request, pk):
    return HttpResponse(f"Product Details Page: {pk}")

