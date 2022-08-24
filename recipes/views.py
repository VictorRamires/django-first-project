from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return HttpResponse('Um retorno qualquer')


def about(request):
    return HttpResponse("Qualquer coisa")


def contact(request):
    return HttpResponse('retorno aleatorio')
