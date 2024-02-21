from django.shortcuts import render
from django.http import HttpResponse

def qna_list(request):
    return HttpResponse("qna_list")

def qnadetails(request, pk):
    return HttpResponse(f"Qna Deteils Page: {pk}")

