from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
  # template = loader.get_template('index.html')
  # return HttpResponse(template.render())
  return render(request, 'index.html')

def signin(request):
  return render(request, 'signin.html')