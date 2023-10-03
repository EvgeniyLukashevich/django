from django.shortcuts import render
from django.http import HttpResponse
from random import randint, choice


def eagle(request):
    return HttpResponse(f'<h1>Ваш результат: {choice(["Орёл", "Решка"])}</h1>')


def cube(request):
    return HttpResponse(f'<h1 style="color: red;">Ваш результат: {randint(1, 6)}</h1>')


def number(request):
    return HttpResponse(f'<h1>Ваш результат: {randint(1, 100)}</h1>')
