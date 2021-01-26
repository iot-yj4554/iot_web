# from django.urls.conf import path
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from polls.models import Question, Choice

# Create your views here.

import logging
logger = logging.getLogger(__name__)

class IndexView(generic.ListView):
    template_name = 'polls/index.html' # 디폴트 네임인 model명(소문자)_list를 커스터마이징
    context_object_name = 'latest_question_list' # 디폴트 네임인 object_list를 커스터마이징

    def get_queryset(self):
        return Question.objects.all().order_by('-pub_date')[:5]

# function-based view
# def index(request):
#     latest_question_list = Question.objects.all().order_by('-pub_date')[:5] # -는 내림차순
#     context = {'latest_question_list': latest_question_list} # HTML로 넘어가는 정보
#     return render(request, 'polls/index.html', context)


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

# function-based view
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question' : question})


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

# function-based view
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question' : question})


def vote(request, question_id):
    logger.debug('vote().question_id : %s' % question_id)
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question' : question,
            'error_message' : "You didn't select a choice",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
