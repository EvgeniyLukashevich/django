from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Framework Django. The 1st Seminar :-)')
