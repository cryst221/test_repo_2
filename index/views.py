from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse


def home(request):
    return render(request, "index/home.html")

def pro(request):
    return HttpResponse("pro")
