from django.http import HttpResponse, response, Http404
from django.shortcuts import render
from django.template import loader

from .models import Question


def index(request):
    # Question 클래스에 대한 QuerySet을 가져옴
    # 게시일자 속성에 대한 내림차순 순서로 최대 5개까지
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
    # 가져온 Question QuerySet을 사용 , 각 Question의 question_text 속성값들ㅇ르
    # list comprehension을 사용해 리스트로 생성
    # 생성한 리스트를 ', ' 문자열의 join 메서드의 인수로 전달, output 에 쉼표 단위로 연결된 문자열을 할당.
    # output = ','.join([q.question_text for q in latest_question_list])


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Qustion does not exit')

    context = {
        'question': question,
    }
    return render(request, 'polls/detail.html', context)


def results(request, question_id):
    response("You're looking at the results of question %s")
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s" % question_id)
