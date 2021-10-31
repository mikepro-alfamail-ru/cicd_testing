from django.http import HttpResponse
from django.shortcuts import render


def home_view(request):
    """пробная домашняя страница"""
    return HttpResponse('Hello from Django! this is a test build')

