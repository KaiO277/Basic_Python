from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("I'm KaiO")

def index1(request):
    return HttpResponse("I;m KaiO-1")
