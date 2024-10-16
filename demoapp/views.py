from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
    return HttpResponse("Hello welcome to django.")

def message(request):
    return HttpResponse("Django is Python full stack web framework.")