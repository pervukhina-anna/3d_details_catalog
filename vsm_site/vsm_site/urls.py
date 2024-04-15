"""
URL configuration for vsm_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from users_lists.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    #Деталь
    #Мы не думаем как информация выводится для того кто редактирует БД; Мы думаем как реализовать для пользователя сайта
    path('api/v1/details/', DetailAPIView.as_view()),

    #Ненужны: 29-30
    path('api/v1/detailsimages/', DetailImageAPIView.as_view()),# возможно ненужны
    path('api/v1/detailsmodels/', Detail3DAPIDetailView.as_view()),# возможно ненужны
    #подробный просмотр
    path('api/v1/detail/<int:pk>/', DetailAPIDetailView.as_view()),
    path('api/v1/detailimage/<int:pk>/', DetailImageAPIView.as_view()),# возможно ненужны
    path('api/v1/detail3dmodel/<int:pk>/', Detail3DAPIDetailView.as_view()),# возможно ненужны

    #Авторизация пользователей
    path('api/v1/auth/login/', UserLoginView.as_view(), name='user-login'),
    path('api/v1/auth/logout/', UserLogoutView.as_view(), name='user-logout'),


    #Заказ
    path('api/v1/orders/', OrdersAPIView.as_view()),
    path('api/v1/order/<int:pk>/', OrdersAPIDetailView.as_view()),

]
