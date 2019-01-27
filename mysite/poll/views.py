from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question,Choice
from django.urls import reverse

# Create your views here.
def index(request):
    question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'question_list': question_list}
    return render(request, 'polls/index2.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice1'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def delete(request):
    question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'question_list': question_list}
    # try:
    #     selected_question = question_list.get(pk=request.POST['choice1'])
    # except (KeyError, Choice.DoesNotExist):
    #     # Redisplay the question voting form.
    #     return render(request, 'polls/delete.html', {
    #         # 'question': question,
    #         'error_message': "You didn't select a choice.",
    #     })
    # else:
    #     selected_question.delete()
    #     selected_question.save()
    return render(request, 'polls/delete.html', context)

def delete2(request):
    question = Question.objects.all()
    # selected_Q = Question.object.get(id=request.POST['question'])
    # return HttpResponse(question)
    try:
        selected_Q = Question.objects.get(id=request.POST['question'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/delete.html', {
            'question_list': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_Q.delete()

        return HttpResponseRedirect(reverse('polls:index'))

