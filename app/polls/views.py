from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("hell world you're at the polls index")
