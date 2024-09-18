"""
URL configuration for vsm_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # Проверка urls
    # path('check/', main_page, name='main_page'),

    #вход на сайт
    path('', LoginUser.as_view(), name='login_user_2'),

    #главная страница
    path('main_page_user/', main_page_user, name='main_page_user'),

    # #результат поиска
    path('search/', search_view, name='search'),

    # #фильтрация по товарам:
    path('details_velaro/', details_velaro, name='details_velaro'),
    path('details_Sample_print/', details_Sample_print, name='details_Sample_print'),
    path('details_desiro/', details_desiro, name='details_desiro'),
    path('details_depot/', details_depot, name='details_depot'),


    #страница определенной детали
    path('detail_page/<int:detail_id>', detail_page, name='detail_page'),

    #механизм оформления товара
    path('view_cart/', view_cart, name='view_cart'),
    path('add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),

    #фильтры по выполненным заказам
    path('view_cart/ready/', cart_order_ready, name='cart_order_ready'),


    # #просмотр заказов для пользователя
    # path('basket/', basket, name='basket'),
    #
    #Добавление детали
    # path('add_page/', add_page, name='add_page'),
    path('add_page_2/', add_page_2, name='add_page_2'),
    #path('add_page/', add_page_view, name='add_page'),

    # #ссылки для оператора
    #Таблица с заказами
    path('operator_page/', operator_page, name='operator_page'),
    #фильтры по заказам
    path('operator_page/order_processing/', order_processing, name='order_processing'),
    path('operator_page/order_in_progress/', order_in_progress, name='order_in_progress'),
    path('operator_page/order_ready/', order_ready, name='order_ready'),

    #изменение статуса заказа

    path('change_status_in_progress/<int:item_id>/', change_order_in_progress, name='change_order_in_progress'),

    path('change_status_ready/<int:item_id>/', change_order_ready, name='change_order_ready'),


    #поиск по пользователям для заказа
    # path('search_user_view/', search_user_view, name='search_user_view'),



]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
