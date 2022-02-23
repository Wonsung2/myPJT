from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def index(request):
    print(">>>>>> user index")
    return render(request, 'user/index.html')

# SELECT * FROM WebUser where user_id = x and user_pwd = x ~ 이런 구문을 써야하지만
# ORM 을 쓴다는 것은 자동으로 테이블과 클래스를 매핑
# ORM : modelName.objects.get()
# select * from WebUser
# orm : modelName.objects.all()
def login(request):
    print('>>>>>> user login')
    if request.method == 'POST':
        print('>>>>request post')
        id = request.POST['id']
        pwd = request.POST['pwd']
        # model - DB(select)
        # 정보를 담는 작업을 필요로 한다
        user = WebUser.objects.get(user_id = id, user_pwd = pwd)
        print('>>>>model value - ', user.user_name)
        context = {'loginUser' : user}
        print('>>>> request param - ', id, pwd)
        return render(request, 'user/ok.html', context)
    else :
        print('>>>>request get')
        # id = request.GET['id']
        # pwd = request.GET['pwd']

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