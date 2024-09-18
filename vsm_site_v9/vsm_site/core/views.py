from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .models import *
from django.views.generic import TemplateView, ListView

from .forms import *
# Create your views here.

# #Проверка
# def main_page(request):
#     return HttpResponse('Hello, World!')

#вход на сайт/авторизация - LoginUser

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'core/login_page_user_2.html'

    def get_success_url(self):
        return reverse_lazy('main_page_user')

#главная страница - main_page_user

def main_page_user(request):
    details_list = Detail.objects.filter(~Q(project='Sample print'))
    context = {
        'details_list': details_list,
    }
    #return HttpResponse("<h1>Проверка работы/логин</h1>")
    return render(request, 'core/main_page_user.html', context=context)

#результат поиска - search_view
#Поисковая строка
def search_view(request):
    query = request.GET.get('query', '')
    results = []

    if query:
        results = Detail.objects.filter((Q(a2v_id__icontains=query) | Q(name__icontains=query))&(~Q(project='Sample print')))

    return render(request, 'core/search_results_2.html', {'results': results, 'query': query})



#фильтрация по товарам: - details_velaro ; details_Sample_print ; details_desiro ; details_depot
#Фильтры для сортировки деталей
def details_desiro(request):
    details_list = Detail.objects.filter(project='Desiro')
    context = {
        'details_list': details_list,
    }
    return render(request, 'core/main_page_user.html', context=context)

def details_velaro(request):
    details_list = Detail.objects.filter(project='Velaro')
    context = {
        'details_list': details_list,
    }
    return render(request, 'core/main_page_user.html', context=context)

def details_depot(request):
    details_list = Detail.objects.filter(project='Depot')
    context = {
        'details_list': details_list,
    }
    return render(request, 'core/main_page_user.html', context=context)

def details_Sample_print(request):
    details_list = Detail.objects.filter(project='Sample print')
    context = {
        'details_list': details_list,
    }
    return render(request, 'core/main_page_user.html', context=context)



#страница определенной детали - detail_page
#Страница детали
def detail_page(request,detail_id):
    detail = get_object_or_404(Detail, pk=detail_id)
    context = {
        'detail': detail,
    }
    #return HttpResponse("<h1>Проверка работы/логин</h1>")
    return render(request, 'core/detail_page.html', context=context)

#Страница - Добавления новой детали

# СТРАНИЦА ДОБАВЛЕНИЯ ДЕТАЛИ
# def add_page(request):
#     #return HttpResponse("<h1>Проверка работы/логин</h1>")
#     return render(request, 'core/add_page.html')
#


# def add_page_2(request):
#     if request.method=='POST':
#         form=AddPostForm(request.POST)
#         if form.is_valid():
#             # try:
#             #     Detail.objects.create(**form.cleaned_data)
#             #     return redirect('main_page_user')
#             # except:
#             #     form.add_error(None, 'Ошибка добавления поста')
#             form.save()
#             return redirect('main_page_user')
#     else:
#         form=AddPostForm()
#     data={
#         'form':form
#     }
#     return render(request, 'core/add_page.html', data)

def add_page_2(request):
    if request.method=='POST':
        form=AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main_page_user')
    else:
        form = AddPostForm()

    return render(request, 'core/add_page.html', {'form': form})

#Механизм простой корзины
#просмотр заказов для пользователя - basket/view_cart
def view_cart(request):
    cart_items = Orders.objects.filter(Q(user=request.user)&(~Q(status='ready')))
    return render(request, 'core/basket_page.html', {'cart_items': cart_items, 'title_1': "Оформленные заказы"})

#Фильтры по корзине
#фильтр Заказ готов - ready
def cart_order_ready(request):
    cart_items = Orders.objects.filter(Q(user=request.user)&Q(status='ready'))
    context = {
        'cart_items': cart_items,
        'title_1': "Выполненные заказы"
    }
    return render(request, 'core/basket_page.html', context=context)


#Добавление в корзину
def add_to_cart(request, product_id):
    query = request.GET.get('query', '')
    detail_name = Detail.objects.get(id=product_id)
    cart_item = Orders.objects.create(detail_name=detail_name, user=request.user)
    cart_item.counted = query
    cart_item.save()
    #переадресация на представление просмотр корзины
    return redirect('view_cart')

#Изначально
# def add_to_cart(request, product_id):
#     detail_name = Detail.objects.get(id=product_id)
#     cart_item = Orders.objects.create(detail_name=detail_name, user=request.user)
#     cart_item.counted = 1
#     cart_item.save()
#     #переадресация на представление просмотр корзины
#     return redirect('view_cart')



# Удалить из корзины
def remove_from_cart(request, item_id):
    cart_item = Orders.objects.get(id=item_id)
    cart_item.delete()
    return redirect('view_cart')






#ссылки для оператора -
#Страница оператора
#Главная страница оператора
def operator_page(request):
    orders_list = Orders.objects.order_by('added_date')
    context = {
        'orders_list': orders_list,
        'title_1': "Все заказы"
    }
    #return HttpResponse("<h1>Проверка работы/логин</h1>")
    return render(request, 'core/main_page_operator.html', context=context)

#фильтры по статусам заказов

#фильтр заказ в обработке - processing
def order_processing(request):
    orders_list = Orders.objects.filter(status='processing')
    context = {
        'orders_list': orders_list,
        'title_1': "Поступившие заказы"
    }
    return render(request, 'core/main_page_operator.html', context=context)

#фильтр заказ в Заказ выполняется - in_progress

def order_in_progress(request):
    orders_list = Orders.objects.filter(status='in_progress')
    context = {
        'orders_list': orders_list,
        'title_1': "Заказы в процессе"
    }
    return render(request, 'core/main_page_operator.html', context=context)
#фильтр Заказ готов - ready
def order_ready(request):
    orders_list = Orders.objects.filter(status='ready')
    context = {
        'orders_list': orders_list,
        'title_1': "Готовые заказы"
    }
    return render(request, 'core/main_page_operator.html', context=context)

#Изменить статус заказа
#Изменить на Заказ выполняется - in_progress

def change_order_in_progress(request, item_id):
    cart_item = Orders.objects.get(id=item_id)
    cart_item.status="in_progress"
    cart_item.save()
    return redirect('operator_page')


#Изменить на Заказ готов - ready
def change_order_ready(request, item_id):
    cart_item = Orders.objects.get(id=item_id)
    cart_item.status="ready"
    cart_item.save()
    return redirect('operator_page')


#Поисковая строка для оператора по пользователям
# #Поисковая строка
# def search_user_view(request):
#     query = request.GET.get('query', '')
#     results = []
#
#     if query:
#         orders_list = Orders.objects.filter(Q(user__icontains=query))
#
#     return render(request, 'core/tabel_orders_user.html', {'orders_list': orders_list, 'query': query})




