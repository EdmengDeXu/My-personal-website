from django.shortcuts import render
from showme.models import ShowMe

def home(request):
    showmes = ShowMe.objects
    return render(request,'home.html',{'showmes':showmes})

def home_en(request):
    showmes = ShowMe.objects
    return render(request,'home_en.html',{'showmes':showmes})
