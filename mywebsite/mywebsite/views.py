from django.shortcuts import render
from showme.models import ShowMe

def home(request):
    showmes = ShowMe.objects
    print(showmes)
    return render(request,'home.html',{'showmes':showmes})