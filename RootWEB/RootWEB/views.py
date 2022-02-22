from django.shortcuts import HttpResponse, render

def index(request) :
    print('>>>>>>>>> root index')
    context = {'intro' : '혈맥강사와 함께하는 장고 프레임워크 웹 개발'}
    return render(request, 'index.html', context)