from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from django.template import loader
from .models import Question
from django.shortcuts import get_object_or_404


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
    # return HttpResponse("Hello, world. You're at the polls index.")
    # Leave the rest of the views (detail, results, vote) unchanged


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'question': question})
#     # return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)