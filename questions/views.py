from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Choice

# Create your views here.
def index(request):
    question = Question.objects.all()

    context = {'question': question}
    return render(request, 'questions/index.html', context)

def vote(request):
    question = Question.objects.get(pk=1)
    select = request.POST.get('selected')
    choice = Choice.objects.get(content=select)
    choice.votes += 1
    choice.save()
    choices = question.choice_set.all()
    context = {
        'question': question,
        'choices': choices,
    }

    return render(request, 'questions/vote.html', context)
