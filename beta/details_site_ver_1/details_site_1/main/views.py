from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from .models import User


# Create your views here.
def login(request):
    # return HttpResponse("<h1>Страница регистрации</h1>")
    return render(request, 'main/login.html')

def user_show(request):
    user_list= User.objects.all()

    context={
        'user_list': user_list,
    }
    return render(request,'main/basket.html', context=context)

#@login_required

def registrate(request):
    # return HttpResponse("<h1>Страница регистрации с нуля</h1>")
    return render(request, 'main/reg_first.html')

def main_page(request):
    #return HttpResponse("<h1>Страница магазина</h1>")
    return render(request, 'main/storage.html')

def detail_page(request):
    #return HttpResponse("<h1>Страница детали</h1>")
    return render(request, 'main/detail_page.html')

def basket(request):
    #return HttpResponse("<h1>Страница детали</h1>")
    return render(request, 'main/basket.html')


