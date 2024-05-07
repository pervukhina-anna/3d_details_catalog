from django.contrib.auth import authenticate, login
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *

# Create your views here.


#КОРЗИНА
class UserCartView(generics.ListCreateAPIView):
    queryset = UserCart.objects.all()
    serializer_class = UserCartSerializer
    permission_classes = [IsAuthenticated & IsAdminUser]

class OrderConfirmationView(generics.ListCreateAPIView):
    queryset = OrderConfirmation.objects.all()
    serializer_class = OrderConfirmationSerializer
    permission_classes = [IsAuthenticated & IsAdminUser]


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

#пользователи Аунтентификация
class UserLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            if created:
                token.delete()  # Delete the token if it was already created
                token = Token.objects.create(user=user)
            return Response({'token': token.key, 'username': user.username, 'role': user.role})
        else:
            return Response({'message': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)

class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        print(request.headers)
        token_key = request.auth.key
        token = Token.objects.get(key=token_key)
        token.delete()

        return Response({'detail': 'Successfully logged out.'})


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
