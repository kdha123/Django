from django.shortcuts import render
# render(request, 템플릿명[,사전형객체])
# 템플릿 변수{{변수}}
# 템플릿 태그 {% 태그 %}
from .models import Member
from django.contrib.auth.hashers import make_password

def list(request):
    mlist = Member.objects.all()
    temp = {'ms': mlist}
    return render(request, 'member/list.html', temp)


def insert(request):
    if request.method == 'GET':
        return render(request, 'member/insert.html')
    elif request.method == 'POST':
        print("디비에 입력")
        username = request.POST['username']
        pw = request.POST['pw']
        repw = request.POST['repw']
        hp = request.POST['hp']
        email = request.POST['email']
        name = request.POST['name']
        msg = {}
        if pw != repw:
            msg['err'] = "비밀번호가 틀렸습니다."
            return render(request, 'member/insert.html')
        elif not (username and pw and hp and repw and name and email):
            msg['err'] = '값을 입력해주세요.'
        else:
            q = Member(username=username, pw=make_password(pw), hp=hp, name=name, email=email)
            q.save()
        return render(request, 'member/insert.html', msg)

