from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("fffffffffffffffffffff")

def about(request):
    return render(request,'navigation/about.html')

def popular_menu(request):
    return render(request,'navigation/popular_menu.html')
