from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.shortcuts import get_object_or_404
from django.urls import reverse
from .models import Question, Choice


# displaying the questions
def index(request):
    question_list = Question.objects.order_by('-p_date')[:5]
    context = {'question_list': question_list}
    return render(request, 'polls/index.html', context)


# showing questions and respective choices
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})


# question and results
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


# voting for a choice
def voting(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls / detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
