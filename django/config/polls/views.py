from django.shortcuts import render

from .models import Question


def index(request):
    return render(request, 'polls/index.html')


def test(request):
    # 삽입, 수정 : save()
    # 삽입
    # q = Question(question_text='좋아하는 색은?', pub_date='2020-01-28')
    # q.save()

    # 수정
    # q = Question(id=2, question_text='좋아하는 운동은?', pub_date='2020-01-28')
    # q.save()

    # 조회
    # qlist = Question.objects.all()
    # qlist = Question.objects.all().order_by('question_text')
    # qlist = Question.objects.all().order_by('-question_text')
    # print(type(qlist))
    # for q in qlist:
    #     print(q.question_text, q.pub_date)

    # 삭제
    q = Question.objects.get(id=2)
    q.delete()
    return render(request, 'polls/test.html')


def insert(request):
    # 입력 5개
    q1 = Question(question_text="좋아하는 음식은?", pub_date='2020-01-28')
    q2 = Question(question_text="좋아하는 연예인은?", pub_date='2020-01-28')
    q3 = Question(question_text="좋아하는 과일은?", pub_date='2020-01-28')
    q4 = Question(question_text="좋아하는 웹툰은?", pub_date='2020-01-28')
    q5 = Question(question_text="좋아하는 영화은?", pub_date='2020-01-28')
    q1.save()
    q2.save()
    q3.save()
    q4.save()
    q5.save()
    return render(request, 'polls/insert.html')


def list(request):
    qlist = Question.objects.all()
    # 딕셔너리 형태로 자료를 넘겨서 html에서 쓰도록 한다.
    temp = {'qs': qlist}

    return render(request, 'polls/list.html', temp)
