from urllib import request
from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request,"home.html")

def contactpage(request):
    return render(request, "contact.html")

