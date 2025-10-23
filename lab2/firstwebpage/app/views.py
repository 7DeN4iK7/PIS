from django.http import HttpResponse
from django.shortcuts import render
from django import template

def home(request):
    return render(request, 'templates/index.html')

def static(request):
    return render(request, 'templates/static_handler.html')

def hello(request):
    response = HttpResponse('Привет, Мир!', content_type="text/plain; charset=utf-8")
    return response