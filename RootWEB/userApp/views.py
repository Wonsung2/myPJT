from django.shortcuts import render

# Create your views here.

def index(request):
    print(">>>>>> user index")
    return render(request, 'user/index.html')

def login(request):
    print('>>>>>> user login')