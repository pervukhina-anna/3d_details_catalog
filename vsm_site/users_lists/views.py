from rest_framework import generics
from django.shortcuts import render
from rest_framework.permissions import *
from .models import *
from .serializers import *


# Create your views here.


##ДЕТАЛИ
#Просмотр деталей
class DetailAPIView(generics.ListAPIView):
    queryset = Detail.objects.all()
    serializer_class = DetailSerializer
    permission_classes = (IsAuthenticated,)


#Под вопросом
#Просмотр Изображений детали
class DetailImageAPIView(generics.ListAPIView):
    queryset = DetailImage.objects.all()
    serializer_class = ImageModelSerializer
    permission_classes = (IsAuthenticated,)

#Под вопросом
#Просмотр 3D-модели детали
class Detail3DAPIView(generics.ListAPIView):
    queryset = Detail3D.objects.all()
    serializer_class = Detail3DSerializer
    permission_classes = (IsAuthenticated,)


#Изменение детали
class DetailAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Detail.objects.all()
    serializer_class = DetailSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

#Изменение Изображения детали
class DetailImageAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DetailImage.objects.all()
    serializer_class = ImageModelSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

#Изменение 3D-модели детали
class Detail3DAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Detail3D.objects.all()
    serializer_class = Detail3DSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


##Пользователи
#Просмотр пользователей
class UsersAPIView(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = (IsAdminUser,)

#Редактирование пользователей
class UsersAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = (IsAdminUser,)

##Заказы

#Список заказов
class OrdersAPIView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = UsersSerializer
    #Подумать над собственным permissions
    permission_classes = (IsAuthenticatedOrReadOnly,)


# Редактирование заказа
class OrdersAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # Подумать над собственным permissions
    permission_classes = (IsAuthenticatedOrReadOnly,)

