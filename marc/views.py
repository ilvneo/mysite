from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Question


def index(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}

    return render(request, 'marc/question_list.html', context)

    #  return HttpResponse("안녕하세요 marc에 오신것을 환영합니다.")


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'marc/question_detail.html', context)


# https://wikidocs.net/70741