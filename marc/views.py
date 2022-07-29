from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer
from django.utils import timezone
from django.contrib import messages
from .forms import QuestionForm


def index(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}

    return render(request, 'marc/question_list.html', context)

    #  return HttpResponse("안녕하세요 marc에 오신것을 환영합니다.")


def question_create(rquest):
    form = QuestionForm()
    return render(reqeust, 'marc/question_form.html', {'form': form})


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'marc/question_detail.html', context)


def answer_create(request, question_id):
    """
    marc 답변등록
    """
    print(request.POST.get('content'))
    question = get_object_or_404(Question, pk=question_id)

    if request.POST.get('content'):
        answer = Answer(question=question, content=request.POST.get('content'), create_date=timezone.now())
    # question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
        answer.save()
    else:
        print("here?")
        messages.warning(request, "내용이 없습니다.")

    return redirect('marc:detail', question_id=question.   id)


# https://wikidocs.net/70741