from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from rest_framework import generics

from .forms import *
# Create your views here.
from .models import *
from .serializers import *
from rest_framework import generics

#Представления для сайта

def login_user(request):
    #return HttpResponse("<h1>Проверка работы/логин</h1>")
    return render(request, 'core/login_page_user.html')

def login_operator(request):
    #return HttpResponse("<h1>Проверка работы/логин</h1>")
    return render(request, 'core/login_page_operator.html')

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'core/login_page_user_2.html'

    def get_success_url(self):
        return reverse_lazy('main_page_user')

class LoginOperator(LoginView):
    form_class = LoginUserForm
    template_name = 'core/login_page_operator_2.html'

    def get_success_url(self):
        return reverse_lazy('main_page_operator')

# def logout_user(request):
#     logout(request)
#     return redirect('login')

def main_page_user(request):
    details_list = Detail.objects.all()
    context = {
        'details_list': details_list,
    }
    #return HttpResponse("<h1>Проверка работы/логин</h1>")
    return render(request, 'core/main_page_user.html',context=context)

def main_page_operator(request):
    orders_list = Orders.objects.order_by('added_date')
    context = {
        'orders_list': orders_list,
    }
    #return HttpResponse("<h1>Проверка работы/логин</h1>")
    return render(request, 'core/main_page_operator.html',context=context)

def detail_page(request,detail_id):
    detail = get_object_or_404(Detail, pk=detail_id)
    context = {
        'detail': detail,
    }
    #return HttpResponse("<h1>Проверка работы/логин</h1>")
    return render(request, 'core/detail_page.html', context=context)


# СТРАНИЦА ДОБАВЛЕНИЯ ДЕТАЛИ
def add_page(request):
    #return HttpResponse("<h1>Проверка работы/логин</h1>")
    return render(request, 'core/add_page.html')

def add_page_2(request):
    if request.method=='POST':
        form=AddPostForm(request.POST, files=request.FILES)
        if form.is_valid():
            try:
                Detail.objects.create(**form.cleaned_data)
                return redirect('main_page_user')
            except:
                form.add_error(None, 'Ошибка добавления поста')

    else:
        form=AddPostForm()
    return render(request, 'core/make_detail.html', {'form': form})

def make_order(request):
    if request.method=='POST':
        form=MakeOrderForm(request.POST)
        if form.is_valid():
            try:
                Orders.objects.create(**form.cleaned_data)
                return redirect('main_page_user')
            except:
                form.add_error(None, 'Ошибка Оформления заказа')

    else:
        form=MakeOrderForm()
    return render(request, 'core/make_order.html', {'form': form})



def basket(request):
    orders_list = Orders.objects.filter(status='processing').order_by('-id')
    context = {
        'orders_list': orders_list,
    }
    #return HttpResponse("<h1>Проверка работы/логин</h1>")
    return render(request, 'core/basket_page.html',context=context)

def search_view(request):
    query = request.GET.get('query', '')
    results = []

    if query:
        results = Detail.objects.filter(a2v_id__icontains=query)

    return render(request, 'core/search_results.html', {'results': results, 'query': query})

def basket_complete(request):
    orders_list = Orders.objects.filter(status='ready').order_by('-id')
    context = {
        'orders_list': orders_list,
    }
    #return HttpResponse("<h1>Проверка работы/логин</h1>")
    return render(request, 'core/basket_page_complete.html', context=context)

#Представления для API

# GET-запрос по выводу всех деталей
class DetailAPIView(generics.ListAPIView):
    queryset = Detail.objects.all()
    serializer_class = DetailSerializer

# GET-запрос по определенной детали
class SingleDetailAPIView(generics.RetrieveAPIView):
    queryset = Detail.objects.all()
    serializer_class = DetailSerializer

# POST-запрос по добавлению детали всех деталей
class CreateDetailAPIView(generics.CreateAPIView):
    queryset = Detail.objects.all()
    serializer_class = DetailSerializer
