from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')      #This is like res.send in express


def about(request):
    return HttpResponse('<h1>About the GermCollector</h1>')