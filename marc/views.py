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
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

logger = logging.getLogger(__name__)


def index(request):
    page = request.GET.get('page', '1') # 페이지
    question_list = Question.objects.order_by('-create_date')
    paginator = Paginator(question_list, 10) # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj}

    return render(request, 'marc/question_list.html', context)

    #  return HttpResponse("안녕하세요 marc에 오신것을 환영합니다.")


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}

    return render(request, 'marc/question_detail.html', context)


@login_required(login_url='common:login')
def question_create(request):
    print("request.method : " + request.method)
    if request.method == 'POST':
        form = QuestionForm(request.POST)

        print("form.is_valid(): " + str(form.is_valid()))
        if form.is_valid():  # 폼 유효하다면
            question = form.save(commit=False)  # 임시 저장하여 question 객체를 리턴한다.
            question.author = request.user # author 속성에 로그인 계정 저장
            question.create_date = timezone.now()  # 실제 저장을 위해 작성일시를 설정한다.
            question.save()  # 데이터를 실제로 저장한다.

            return redirect('marc:index')
    else:
        form = QuestionForm()
    context = {'form': form}

    return render(request, 'marc/question_form.html', context)


@login_required(login_url='common:login')
def answer_create(request, question_id):
    """
    marc 답변등록
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user  # author 속성에 로그인 계정 저장
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


@login_required(login_url='common:login')
def question_modify(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('pybo:detail', question_id=question.id)
    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.modify_date = timezone.now()  # 수정일시 저장
            question.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = QuestionForm(instance=question)
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)



# https://wikidocs.net/71445
