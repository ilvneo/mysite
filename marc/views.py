from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer
from django.utils import timezone
from django.contrib import messages
from .forms import QuestionForm, AnswerForm
import logging
from django.http import HttpResponseNotAllowed

logger = logging.getLogger(__name__)


def index(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}

    return render(request, 'marc/question_list.html', context)

    #  return HttpResponse("안녕하세요 marc에 오신것을 환영합니다.")


def question_create(request):
    print("request.method : " + request.method)
    if request.method == 'POST':
        form = QuestionForm(request.POST)

        print("form.is_valid(): " + str(form.is_valid()))
        if form.is_valid():  # 폼 유효하다면
            question = form.save(commit=False)  # 임시 저장하여 question 객체를 리턴한다.
            question.create_date = timezone.now()  # 실제 저장을 위해 작성일시를 설정한다.
            question.save()  # 데이터를 실제로 저장한다.

            return redirect('marc:index')
    else:
        form = QuestionForm()
    context = {'form': form}

    return render(request, 'marc/question_form.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}

    return render(request, 'marc/question_detail.html', context)


def answer_create(request, question_id):
    """
    marc 답변등록
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('marc:detail', question_id=question.id)
    else:
        return HttpResponseNotAllowed('Only POST is possible.')
    context = {'question': question, 'form': form}
    return render(request, 'marc/question_detail.html', context)

    # if request.POST.get('content'):
    #     answer = Answer(question=question, content=request.POST.get('content'), create_date=timezone.now())
    #     # question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    #     answer.save()
    # else:
    #     print("here?")
    #     messages.warning(request, "내용이 없습니다.")
    #
    # return redirect('marc:detail', question_id=question.id)

# https://wikidocs.net/70741
