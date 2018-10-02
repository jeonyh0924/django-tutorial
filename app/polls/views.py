from django.http import HttpResponse, response
from django.shortcuts import render


def index(request):
    return HttpResponse("hell world you're at the polls index")


def detail(reqest, question_id):
    return HttpResponse("You're looking at question %s" % question_id)


def results(request, question_id):
    response("You're looking at the results of question %s")
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s" % question_id)
