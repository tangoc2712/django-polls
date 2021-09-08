from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Đây là response haahaaha!!!")


