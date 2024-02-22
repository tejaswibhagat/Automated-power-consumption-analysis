from django.shortcuts import render
from django.http import HttpResponse,request

# Create your views here.

def index(request):
    return HttpResponse("Index Dashboard")

def home(request):
    return render(request, 'dashboard/homepage.html')
