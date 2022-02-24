from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def index(request):
    print(">>>>>> user index")
    if request.session.get('user_name') :
        print('>>>>login session exist!!')
        context ={
            'session_user_name' : request.session.get('user_name') ,
            'session_user_id': request.session.get('user_id'),
        }
        return render(request, 'user/ok.html', )
    else :
        return render(request, 'user/index.html')

# SELECT * FROM WebUser where user_id = x and user_pwd = x ~ 이런 구문을 써야하지만
# ORM 을 쓴다는 것은 자동으로 테이블과 클래스를 매핑
# ORM : modelName.objects.get()
# select * from WebUser
# orm : modelName.objects.all()
#session tracking m
def login(request):
    print('>>>>>> user login')
    if request.method == 'POST':
        print('>>>>request post')
        id = request.POST['id']
        pwd = request.POST['pwd']
        # model - DB(select)
        # 정보를 담는 작업을 필요로 한다
        context = {}
        try :
            user = WebUser.objects.get(user_id = id, user_pwd = pwd)
            # 세션을 만드는 과정
            request.session['user_name'] = user.user_name
            request.session['user_id'] = user.user_id
            # 세션을 심는 과정
            context['session_user_name'] = request.session['user_name']
            context['session_user_id'] = request.session['user_id']
            return render(request, 'user/ok.html', context)
        except Exception as e :
            context['error'] = 'invalid id, pwd'
            return render(request, 'user/index.html', context)
    # else :
    #     print('>>>>request get')
    #     # id = request.GET['id']
    #     # pwd = request.GET['pwd']

def list(request):
    print('>>>>user list')
    division = request.GET['category']
    print('>>>>param - ', division)
    # model - select * from table where category = sport
    users = WebUser.objects.all()
    for u in users :
        print('>>>>' , u.user_name)
    context = { 'users' : users}
    return render(request, 'user/list.html', context)

def detail(request):
    print('>>>>user detail')
    id = request.GET['id']
    print('>>>> param id -', id)
    user = WebUser.objects.get(user_id = id)
    if user is not None :
        context = {'user' : user}
    else :
        context = {'error' : '사용자 정보가 존재하지 않습니다!!'}
    return render(request, 'user/detail.html', context)

def registerForm(request):
    print('user register Form - ')
    return render(request, 'user/join.html')

def join(request):
    print('>>>>user join - ')
    id = request.POST['id']
    pwd = request.POST['pwd']
    name = request.POST['name']
    print('>>>> param values - ', id, pwd, name)
    # insert into table_name(id, pwd, name) values('', '', '')
    # ORM : modelName( attr - value ).save()
    WebUser(user_id= id, user_pwd = pwd, user_name = name).save()
    # return render(request, 'user/index.html')
    return redirect('index')

def logout(request):
    print('>>>>user logout')
    # 세션을 삭제
    request.session['user_name'] = {}
    request.session['user_id'] = {}
    request.session.modified = True

    # 새로운 request url을 정의할 때
    return redirect('main')