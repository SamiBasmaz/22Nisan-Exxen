from django.shortcuts import render
from .models import *



# Create your views here.

def index(request):
    films = Film.objects.all()
    return render(request, "index.html", {'films': films})




