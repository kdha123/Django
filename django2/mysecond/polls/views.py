from django.shortcuts import render
from .models import Question, Choice
from django.shortcuts import get_object_or_404

def list(request):
    qlist = Question.objects.all()
    return render(request, 'polls/list.html', {'ql': qlist})


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # choice = get_object_or_404(Choice)
    return render(request, 'polls/detail.html', {'q': question})
